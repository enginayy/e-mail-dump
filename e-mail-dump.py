import aiohttp
import asyncio
import re
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
discovered_urls = set()
found_emails = set()
semaphore = asyncio.Semaphore(10)  # Up to 10 requests at the same time

async def get_emails_from_page(content):
    return set(re.findall(EMAIL_REGEX, content))

async def fetch(session, url):
    async with semaphore:
        try:
            async with session.get(url, timeout=10) as response:
                if "text/html" not in response.headers.get("Content-Type", ""):
                    return None
                return await response.text()
        except Exception as e:
            print(f"[!] Error: {e} - {url}")
            return None

async def crawl_website(base_url):
    queue = [base_url]
    async with aiohttp.ClientSession() as session:
        while queue:
            url = queue.pop(0)
            if url in discovered_urls:
                continue
            discovered_urls.add(url)
            page_content = await fetch(session, url)
            if not page_content:
                continue
            emails = await get_emails_from_page(page_content)
            for email in emails:
                if email not in found_emails:
                    print(f"[+] Found email: {email}")
                    found_emails.add(email)
                    with open("emails.txt", "a") as f:
                        f.write(email + "\n")
            soup = BeautifulSoup(page_content, 'lxml')
            for link in soup.find_all("a", href=True):
                full_url = urljoin(base_url, link['href'])
                if urlparse(full_url).netloc == urlparse(base_url).netloc:
                    queue.append(full_url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Asynchronous Web Browser")
    parser.add_argument("-u", "--url", required=True, help="https://site.com")
    args = parser.parse_args()
    print(f"[*] Scan begins: {args.url}")
    asyncio.run(crawl_website(args.url))
    print("[*] The scan is complete. The emails were saved in the 'emails.txt' file.")

Async Email Scraper

This project asynchronously scans a specified website to find and save email addresses. It utilizes aiohttp and BeautifulSoup libraries for efficient web crawling.

Features

Asynchronous Crawling: Uses aiohttp for fast and efficient web scraping.

Email Extraction: Identifies email addresses on web pages using regular expressions (regex).

Internal Link Tracking: Follows links within the same domain to maximize email discovery.

File Logging: Automatically saves found emails into the emails.txt file.

Requirements

Install the necessary dependencies:

          pip install aiohttp beautifulsoup4 lxml

Usage

Run the following command to start scraping emails from a specified website:

          python3 e-mail-dump.py -u https://targetsite.com

How It Works

Web Pages Are Fetched: The specified URL's content is fetched asynchronously using aiohttp.

Emails Are Extracted: Email addresses are extracted from the page content using regex.

Links Are Followed: Internal links within the same domain are discovered and added to the queue.

Results Are Saved: Found email addresses are saved in the emails.txt file.

Example Output

[*] Scan begins: https://targetsite.com
[+] Found email: contact@example.com
[+] Found email: info@targetsite.com
[*] The scan is complete. The emails were saved in the 'emails.txt' file.

Notes

May not work on sites that block bots.

Crawling large sites may increase network usage.

Ethical guidelines and legal considerations should be followed during usage.

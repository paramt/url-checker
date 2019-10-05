#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from urlextract import URLExtract
import requests

# URLs to skip over
blacklisted = os.getenv("INPUT_BLACKLIST", "").split(",")

files = os.getenv('INPUT_FILES').split(",")
repo = os.getenv("GITHUB_REPOSITORY")
links = []
exit_status = 0

for file in files:
    print(f"Collecting URLs from {file}")
    filepath = "https://raw.githubusercontent.com/" + repo + "/master/" + file
    text = requests.get(filepath).text

    extractor = URLExtract()
    file_links = extractor.find_urls(text)

    links += file_links

print("Cleaning up list of URLs")

# Remove mailto links
links = [url for url in links if "mailto://" not in url]

# Remove blacklisted links
for link in links:
    if link in blacklisted:
        links.remove(link)
        print(f"Removed {link}")

print("Checking all URLs")

for url in links:
    try:
        request = requests.get(url)
        if request.status_code == 200:
            print(f"✓ 200 {url}")
        elif request.status_code >= 400:
            print(f"✕ {request.status_code} {url}")
            exit_status = 1
        else:
            print(f"⚪ {request.status_code} {url}")

    except:
        print(f"✕ ERR {url}")

        # Continue through all URLs but fail test at the end
        exit_status = 1
        continue

exit(exit_status)

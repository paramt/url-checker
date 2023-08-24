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

def remove_duplicates(urls):
    return list(set(urls))


def get_test_from_file(file):
    # Assume the local file has been checked out in the action
    try:
        with open('./' + file) as f:
            text = f.readlines()
            print("Found file in the locally checked out repo")
            return ' '.join(text)
    except FileNotFoundError as e:
        print("Could not find file checked out locally, falling back to using public link")

    # Fall-back to pulling from the public URL for backawards comaptibility
    try:
        filepath = "https://raw.githubusercontent.com/" + repo + "/master/" + file
        r = requests.get(filepath)
        r.raise_for_status()
        return r.text
    except requests.exceptions.HTTPError as err:
        print("Could not find file using fallback public link")    


for file in files:
    
    text = get_test_from_file(file)

    extractor = URLExtract()
    file_links = extractor.find_urls(text)

    # Remove mailto links
    links = [url for url in file_links if "mailto://" not in url]
    linksToRequest = []

    # Remove blacklisted links
    for link in links:
        if link in blacklisted:
            print(f"Removed {link}")
        else:
            linksToRequest.append(link)

    print(f"Checking URLs from {file}")

    # Remove Duplicate links
    linksToRequest = remove_duplicates(linksToRequest)

    print(f"Removing duplicate URLs from {file}")

    for url in linksToRequest:
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

    # Newline to separate URLs from different files
    print()

exit(exit_status)
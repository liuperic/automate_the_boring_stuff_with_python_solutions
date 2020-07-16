#!/usr/bin/env python3
# link_verification.py - Given the URL, saves every linked page on url to a file.

import bs4, requests

url = input('Please enter the URL of the site you would like to save linked pages to: ')

try:
    res = requests.get(url)
    res.raise_for_status()

    page_soup = bs4.BeautifulSoup(res.text, 'html.parser')
    page_links = page_soup.select('a')

    file_links = open('file_links.txt', 'w').close()
    file_links = open('file_links.txt', 'a')

    for link in page_links:
        link = link.get('href')
        if not link.startswith('https'):
            link = url + link

        link_res = requests.get(link)
        link_res.raise_for_status()

        if link_res.status_code == 404:
            print(f'Bad link: {link}')
        else:
            file_links.write(link + '\n')

    file_links.close()

except Exception as exc:
    print(f'Invalid page link: {exc}')



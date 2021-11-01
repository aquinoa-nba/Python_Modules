#!/usr/bin/env python3

from sys import argv
from requests import get
from bs4 import BeautifulSoup


step = 0
all_pages = []


def check_page(pagename):
    if pagename in all_pages:
        print('It leads to an infinite loop !')
        exit(0)
    all_pages.append(pagename)
    if pagename == 'Philosophy':
        for road in all_pages:
            print(road)
        print(f'{step} roads from {all_pages[0]} to philosophy !')
        exit(0)


def parse_soup(soup):
    block = soup.find(class_='mw-parser-output')
    p_tags = block.findAll('p')
    for p in p_tags:
        if p.find_parent() != block:
            continue
        links = p.findAll('a')
        for link in links:
            href = link.get('href')
            if href.find('.ogg') == -1 and href.find('/wiki/') == 0 and href.find(':') == -1:
                soup_maker(link.get('title'))
    print('It leads to a dead end !')
    exit(0)


def soup_maker(pagename):
    global step
    step += 1
    response = get('https://en.wikipedia.org/wiki/' + pagename)
    if response.status_code != 200:
        print('Error:', response.url, response.reason)
        exit(1)
    soup = BeautifulSoup(response.content, "html.parser")
    check_page(soup.title.text.replace(' - Wikipedia', ''))
    parse_soup(soup)


if __name__ == '__main__':
    if len(argv) != 2:
        print('Error: Wrong numbers of arguments')
    else:
        try:
            soup_maker(argv[1])
        except Exception as exc:
            print(exc)
    exit(1)

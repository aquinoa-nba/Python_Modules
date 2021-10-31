#!/usr/bin/env python3

from sys import argv
from requests import get
from bs4 import BeautifulSoup


step = 0
all_pages = []
dead_end = []


def dead_end_maker():
    response = get('https://en.wikipedia.org/wiki/Category:All_dead-end_pages')
    all_dead_ends = BeautifulSoup(response.content, "html.parser").find(class_='mw-category-generated').findAll('a')
    for link in all_dead_ends:
        href = link.get('href')
        if href.find(':') == -1:
            dead_end.append(href.replace('/wiki/', ''))


def check_page(pagename):
    if pagename in all_pages:
        print('It leads to an infinite loop !')
        exit(1)
    elif pagename in dead_end:
        print('It leads to a dead end !')
        exit(1)
    all_pages.append(pagename)
    if pagename == 'Philosophy':
        for road in all_pages:
            print(road)
        print(f'{step} roads from { all_pages[0]} to philosophy !')
        exit(0)


def parse_soup(soup):
    block = soup.find(class_='mw-parser-output')
    if not block:
        print(f"Error: page {soup.title.text.replace(' - Wikipedia', '')} not found")
        exit(1)
    p_tags = block.findAll('p')
    for p in p_tags:
        if p.find_parent() != block:
            continue
        links = p.findAll('a')
        for link in links:
            href = link.get('href')
            if href.find('.ogg') == -1 and href.find('/wiki/') == 0 and href.find(':') == -1:
                title = link.get('title')
                soup_maker(title.replace('_', ' '))


def soup_maker(pagename):
    global step
    step += 1
    response = get('https://en.wikipedia.org/wiki/' + pagename)
    soup = BeautifulSoup(response.content, "html.parser")
    check_page(soup.title.text.replace(' - Wikipedia', ''))
    parse_soup(soup)


if __name__ == '__main__':
    if len(argv) != 2:
        print('Error: Wrong numbers of arguments')
    else:
        try:
            dead_end_maker()
            soup_maker(pagename=argv[1])
        except Exception as exc:
            print(exc)

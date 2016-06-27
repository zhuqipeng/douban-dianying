# -*- coding: utf-8 -*-

import sys
import logging
import requests
from bs4 import BeautifulSoup

logging.captureWarnings(True)


def film_name(soup):
    return soup.find('span', attrs={'property': 'v:itemreviewed'}).text


def film_actor(soup):
    tags = soup.find('span', attrs={'class': 'actor'}).findAll('a')
    return map(lambda x: x.text, tags)


def main(url=None):
    # url = 'https://movie.douban.com/subject/4811813/'
    rep = requests.get(url)
    soup = BeautifulSoup(rep.text)

    name = film_name(soup)
    actor = film_actor(soup)

    print u'影片名：', name
    print u'演员：', u' / '.join(actor)


if __name__ == '__main__':
    main(sys.argv[1])

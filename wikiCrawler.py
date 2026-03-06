from urllib.request import urlopen, Request
from urllib.request import HTTPError
from urllib.request import URLError
import re

from bs4 import BeautifulSoup

def urlCrawler(url):
    req = Request(url, headers= {'User-Agent': 'Mozila/5.0'})
    html = urlopen(req)
    bs = BeautifulSoup(html, 'html.parser')
    #html 에서 a 태그를 가져온다. 이때 속성값으로 href 를 가지면 그걸 출력한다.
    #href 속성은 링크가 연결될 목적지를 값으로 가진다.
    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            print(link.attrs['href'])


def main():
    urlCrawler('https://en.wikipedia.org/wiki/Kevin_Bacon')


if __name__ == "__main__":
    main()


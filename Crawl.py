# coding=utf-8
import asyncio
import os
import re
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup as bs
from gne import GeneralNewsExtractor
from pyppeteer import launch
from lxml import etree
headers = {
   'User-Agent ': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
   }
'''
爬虫类爬取新闻等语料数据
'''

class Crawl():
    def __init__(self):
        pass
    def get_news(self):
        url = 'https://news.qq.com/'
        res = requests.get('url',headers=headers)
        res.encoding = 'utf-8'
        rest = res.text

        soup = bs(rest,'lxml')
        print(soup.find_all('p',attrs={'class':'brief'}).children.string)
        pass
    def get_jok(self):
        pass

async def main():
    extractor = GeneralNewsExtractor
    url = 'http://politics.people.com.cn/'
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    page_text = await  page.content()

    reslute = extractor.extract(page_text)
    print(reslute)
    '''
    soup = bs(rest, 'lxml')
    print(rest)
    print(soup.h4.string)
    print(soup.find_all('div', attrs={'class': "m-recommend"}))
    '''
if __name__ == '__main__':
    asyncio.run(main())
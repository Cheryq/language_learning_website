url='http://www.hxen.com/yingyuwenzhang/'
from collections import UserList
import requests
import pymysql
from lxml import etree
def get_content(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    allUrl=tree.xpath('//h3[@ class="fz18 YaHei fbold"]/a/@href')
    allTitle=tree.xpath('//h3[@class="fz18 YaHei fbold"]//text()')
    print(allTitle)
    print(allUrl)
#get_content(url)
url='http://www.hxen.com/yingyuwenzhang/computer-network/security/2008-06-25/42309.html'

def get_text(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    content=tree.xpath('//div[@ id="arctext"]/text()')
    strRes=""
    print(content)
get_text(url)
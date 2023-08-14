import requests
import pymysql
from lxml import etree
def get_content(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    #title=tree.xpath('//div[@id="teacher-box"]/h2//text()')
    content=tree.xpath('//div[@class="w-cell"]//li//a/@href')
    print(content)
get_content('https://www.nhk.or.jp/lesson/chinese/vocabulary/list/')



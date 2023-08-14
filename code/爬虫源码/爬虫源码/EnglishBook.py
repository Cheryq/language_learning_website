url='https://book.douban.com/tag/%E5%BE%B7%E8%AF%AD'
from collections import UserList
import requests
import pymysql
from lxml import etree
allDes=[]
#url='http://de.qsbdc.com/deword/word_list.php?letter_id=1&&tag=all&&page_id=1'
#list=[35,16,43,26,33,18,10,7,15,4,1,10,22,6,7,37,3,24,26,18,2,10,1,1,1,1]
def get_content(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    #title=tree.xpath('//div[@id="teacher-box"]/h2//text()')

    content=tree.xpath('//div[@class="info"]/h2/a/text()')
    content2=tree.xpath('//div[@class="info"]//div[@class="pub"]/text()')
    #content3=tree.xpath('//div[@class="pic"]//img')
    for i in range(0,len(content)):
        strTemp=''
        for j in range(0,len(content[i])):

            if(content[i][j]!='\n' and content[i][j]!=' '):
                strTemp+=content[i][j]

        content[i]=strTemp
    for i in range(0,len(content2)):
        strTemp=''
        for j in range(0,len(content2[i])):
            if(content2[i][j]=='/'):
                break            
            if(content2[i][j]!='\n' and content2[i][j]!=' '):
                strTemp+=content2[i][j]
        content2[i]=strTemp
    #print(content)
    global bookName
    for i  in range(0,len(content)):
        if(content[i]=='' or  content[i]==' '):
            continue
        bookName.append(content[i])
    global author
    for i in range(0,len(content2)):

        author.append(content2[i])
    nameAndauthor=[]
    nameAndauthor.append(bookName)
    nameAndauthor.append(author)
    print(bookName)
    print(author)
    print(len(bookName))
    print(len(author))

    return nameAndauthor
    


def get_pic(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    #title=tree.xpath('//div[@id="teacher-box"]/h2//text()')
    #content=tree.xpath('//div[@class="info"]/h2/a/text()')
    #content2=tree.xpath('//div[@class="info"]//div[@class="pub"]/text()')
    global allPic
    allPic=tree.xpath('//div[@class="pic"]//img/@src')
   

def get_url(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    global allUrl
    allUrl=tree.xpath('//a[@class="nbg"]/@href')
    print(allUrl)
    
def get_description(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    content=tree.xpath('//div[@class="intro"]//p/text()')
    strRes=''
    for i in range(0,len(content)-1):
        strRes+=content[i]
    allDes.append(strRes)
bookName=[]
author=[]
allPic=[]
allUrl=[]
get_pic(url)
get_content(url)
get_url(url)

#get_content(url)


print(len(bookName))
print(len(author))
print(len(allPic))
print(len(allUrl))


    #print(strRes)
    #print(content)
#get_description('https://book.douban.com/subject/35143790/')
for i in range(0,len(allUrl)):
    get_description(allUrl[i])
    print(str(i)+"done")


conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',charset='utf8')
cursor = conn.cursor()  # 创建游标，用于与数据库交互
#cursor.execute('drop database if exists article1')  # execute为执行SQL语句，此处的含义是如果存在数据库"test"，就把该数据库删掉
#cursor.execute('create database if not exists article1 character set utf8mb4 collate utf8mb4_general_ci')  # 如果不存在test数据库，则创建
conn.commit()  # commit()函数为手动提交对于数据库的修改

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')

cursor = conn.cursor() 
cursor.execute('CREATE TABLE `GermanBook` (`id` int NOT NULL,                `name` varchar(200) DEFAULT NULL,               `author` varchar(1000) DEFAULT NULL,               `description` varchar(10000) DEFAULT NULL,                `pic` varchar(200) DEFAULT NULL,       PRIMARY KEY (`id`)          ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4')
conn.commit()

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')


cursor = conn.cursor()
idIndex=0
i=0
while(i<len(author)):
    
    try:
        cursor.execute('INSERT INTO GermanBook (id,name,author,description,pic)       VALUES (%s,%s,%s,%s,%s)' ,(idIndex,bookName[i],author[i],allDes[i],allPic[i]))
        print("make"+str(idIndex))
        idIndex+=1
        i=i+1
    except:

        idIndex+=1
        i=i+1
   
print("done")
conn.commit()

from collections import UserList
import requests
import pymysql
from lxml import etree
def get_content(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    #title=tree.xpath('//div[@id="teacher-box"]/h2//text()')
    content=tree.xpath('//div[@class="text-box"]//text()')
    #print(content)
    #print(type(content))
    #for i in content:
    #    print(i)
    #print(title)
    #print(content)
    #print(type(content))
    copyContent=content
    #print(len(content))
    for i in range(int(len(content))):
        #print(content[i])
        if('\n' in content[i]):
            copyContent[i]=""

    #print(content[5][4])
    #print(copyContent)
    index=0
    while(index<len(copyContent)):
        if(copyContent[index]==""):
            del copyContent[index]
            index=index-1
            if(index==-1): 
                index=0
        else:
            index=index+1
    #print(copyContent)
    #print(len(copyContent))
    return copyContent 
#get_content('https://www.nhk.or.jp/lesson/zh/lessons/09.html#vocabulary')
allUrl=[]
for i in range(1,49):
    if(i<10):
        temp='https://www.nhk.or.jp/lesson/zh/lessons/0'+str(i)+'.html#vocabulary'
    else:
        temp='https://www.nhk.or.jp/lesson/zh/lessons/'+str(i)+'.html#vocabulary'
    allUrl.append(temp)

allRes=[]
for i in allUrl:
    for j in get_content(i):
        allRes.append(j)
    print(i)
print(allRes)

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',charset='utf8')
cursor = conn.cursor()  # 创建游标，用于与数据库交互
#cursor.execute('drop database if exists article1')  # execute为执行SQL语句，此处的含义是如果存在数据库"test"，就把该数据库删掉
#cursor.execute('create database if not exists article1 character set utf8mb4 collate utf8mb4_general_ci')  # 如果不存在test数据库，则创建
conn.commit()  # commit()函数为手动提交对于数据库的修改

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')

cursor = conn.cursor() 
cursor.execute('CREATE TABLE `JanpanseWord2` (`id` int NOT NULL,                `word` varchar(200) DEFAULT NULL,               `prononce` varchar(100) DEFAULT NULL,               `translation` varchar(1000) DEFAULT NULL,       PRIMARY KEY (`id`)          ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4')
conn.commit()

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')


cursor = conn.cursor()
i=0
while(i<len(allRes)):
    
    cursor.execute('INSERT INTO JanpanseWord2 (id,word,prononce, translation)       VALUES (%s,%s,%s, %s)' ,(i/3,allRes[i],allRes[i+1],allRes[i+2]))
    i=i+3
    print("make"+str(i))

    
print("done")
conn.commit()



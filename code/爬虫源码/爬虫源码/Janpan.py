import requests
import pymysql
from lxml import etree
def get_content(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    title=tree.xpath('//div[@id="teacher-box"]/h2//text()')
    content=tree.xpath('//div[@id="teacher-box"]/text()')
    #print(content)
    #print(type(content))
    #for i in content:
    #    print(i)
    #print(title)
    titleRes=""
    contentRes=""
    for i in title:
        titleRes+=i
    for i in content:
        contentRes+=i
    allRes=[]
    allRes.append(titleRes)
    allRes.append(contentRes)
    return  allRes
#temp=get_content('https://www.nhk.or.jp/lesson/chinese/teacher/1.html')
res=[]
allUrl=[]
for i in range(1,49):
    allUrl.append("https://www.nhk.or.jp/lesson/chinese/teacher/"+str(i)+".html")
print(allUrl)
for i in allUrl:
    temp=get_content(i)
    res.append(temp)
    print(str(i)+"done")

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',charset='utf8')
cursor = conn.cursor()  # 创建游标，用于与数据库交互
#cursor.execute('drop database if exists article1')  # execute为执行SQL语句，此处的含义是如果存在数据库"test"，就把该数据库删掉
#cursor.execute('create database if not exists article1 character set utf8mb4 collate utf8mb4_general_ci')  # 如果不存在test数据库，则创建
conn.commit()  # commit()函数为手动提交对于数据库的修改

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')

cursor = conn.cursor() 
cursor.execute('CREATE TABLE `JanpanseLearn` (`id` varchar(100) NOT NULL,                `name` varchar(200) DEFAULT NULL,               `description` varchar(10000) DEFAULT NULL,       PRIMARY KEY (`id`),               UNIQUE KEY `name` (`name`) USING BTREE          ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4')
conn.commit()

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')


cursor = conn.cursor()
for i in range(len(res)):
    try:
        cursor.execute('INSERT INTO JanpanseLearn (id,name, description)       VALUES (%s,%s, %s)' ,(str(i),res[i][0],res[i][1]))
        print("make"+str(i))
    except:
        continue
print("done")
conn.commit()
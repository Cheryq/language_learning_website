from collections import UserList
import requests
import pymysql
from lxml import etree
url='http://de.qsbdc.com/deword/word_list.php?letter_id=1&&tag=all&&page_id=1'
list=[35,16,43,26,33,18,10,7,15,4,1,10,22,6,7,37,3,24,26,18,2,10,1,1,1,1]
def get_content(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    #title=tree.xpath('//div[@id="teacher-box"]/h2//text()')
    content=tree.xpath('//span[@class="hidden_1_1"]//text()')
    chinContent=tree.xpath('//span[@class="hidden_3_1"]//text()')
    #proContent=tree.xpath('//span[@class="hidden_2_1"]//text()')
    #print(content)
    #print(chinContent)
    #print(len(content))
    #print(len(chinContent))
    for i in range(0,len(chinContent)):
        allContent.append(content[i])
        allChinContent.append(chinContent[i])
allContent=[]
allChinContent=[]
for i in range(0,len(list)):
    for j in range(0,list[i]):
        #url='http://de.qsbdc.com/deword/word_list.php?letter_id='+str(i+1)+'&&tag=all&&page_id='+str(j+1)
        url='http://fr.qsbdc.com/word/word_list.php?letter_id='+str(i+1)+'&&tag=all&&page_id='+str(j+1)        #url='http://sp.qsbdc.com/word/word_list.php?letter_id='+str(i+1)+'&&tag=all&&page_id='+str(j+1)
        get_content(url)
    print("i"+str(i)+"done")
print(allContent)
print(len(allContent)) 
print(len(allChinContent))

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',charset='utf8')
cursor = conn.cursor()  # 创建游标，用于与数据库交互
#cursor.execute('drop database if exists article1')  # execute为执行SQL语句，此处的含义是如果存在数据库"test"，就把该数据库删掉
#cursor.execute('create database if not exists article1 character set utf8mb4 collate utf8mb4_general_ci')  # 如果不存在test数据库，则创建
conn.commit()  # commit()函数为手动提交对于数据库的修改

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')

cursor = conn.cursor() 
cursor.execute('CREATE TABLE `French` (`id` int NOT NULL,                `word` varchar(200) DEFAULT NULL,               `translation` varchar(1000) DEFAULT NULL,       PRIMARY KEY (`id`)          ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4')
conn.commit()

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')


cursor = conn.cursor()
i=0
while(i<len(allContent)):
    
    cursor.execute('INSERT INTO French (id,word,translation)       VALUES (%s,%s,%s)' ,(i,allContent[i],allChinContent[i]))
    i=i+1
    print("make"+str(i))
   
print("done")
conn.commit()

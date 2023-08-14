from collections import UserList
import requests
import pymysql
from lxml import etree
url='https://www.douban.com/doulist/469012/'
def get_content(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    print(response)
    tree=etree.HTML(response.text)
    content=tree.xpath('//div[@class="post"]/a/img/@src')
    allUrl=tree.xpath('//div[@class="title"]/a/@href')
    title=tree.xpath('//div[@class="title"]/a//text()')
    director=tree.xpath('//div[@class="abstract"]//text()[1]')
    type=tree.xpath('//div[@class="abstract"]//text()[3]')
    #print(type)
    titleRes=[]
    directorRes=[]
    #print(title)
    for i in range(0,len(title)):
        strTemp=""
        if(title[i]=='' or title[i]==' '):
            continue        
        for j in range(0,len(title[i])):
            if(title[i][j]==' ' or title[i][j]=='\n'):
                continue
            else:
                strTemp+=title[i][j]
        titleRes.append(strTemp)

    for i in range(0,len(director)):
        strTemp=""
        find=False
        if(director[i]=='' or director[i]==' '):
            continue
        for j in range(0,len(director[i])):
            if(director[i][j]==':'):
                find=True
                continue
            elif (director[i][j]==' ' or director[i][j]=='\n'):
                continue
            if(find):
                strTemp+=director[i][j]
        directorRes.append(strTemp)

    typeRes=[]
    for i in range(0,len(type)):
        strTemp=""
        find=False
        for j in range(0,len(type[i])):
            if(type[i][j]==':'):
                find=True
                continue
            elif (type[i][j]==' ' or type[i][j]=='\n'):
                continue
            if(find):
                strTemp+=type[i][j]
        typeRes.append(strTemp)

    titleResNew=[]
    for i in range(0,len(titleRes)):
        if(titleRes[i]=='' or titleRes[i]==' '):
            continue
        titleResNew.append(titleRes[i])
    print(content)        
    print(titleResNew)
    print(directorRes)
    print(typeRes)
    print(allUrl)
    print(len(content))        
    print(len(titleResNew))
    print(len(directorRes))
    print(len(typeRes))
    print(len(allUrl))
    nameAtitleAdirAtype=[]
    nameAtitleAdirAtype.append(content)
    nameAtitleAdirAtype.append(titleResNew)
    nameAtitleAdirAtype.append(directorRes)
    nameAtitleAdirAtype.append(typeRes)   
    nameAtitleAdirAtype.append(allUrl)
    return nameAtitleAdirAtype
nameAtitleAdirAtype=get_content(url)

detailUrl='https://movie.douban.com/subject/2284851/'
def get_description(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    #print(response)
    tree=etree.HTML(response.text)
    intro=tree.xpath('//span[@property="v:summary"]//text()')
    #print(director)
    #print(intro)
    res=""
    for i in range(0,len(intro)):
        for j in range(0,len(intro[i])):
            if(intro[i][j]=='\n' or intro[i][j]=='\u3000' or intro[i][j]==' '):
                continue
            else:
                res=res+intro[i][j]
    #print(res)
    return res

intro=[]
for i in range(0,len(nameAtitleAdirAtype[4])):
    res=get_description(nameAtitleAdirAtype[4][i])
    intro.append(res)
#print(intro)
nameAtitleAdirAtype.append(intro)
#print(nameAtitleAdirAtype)
    

#//*[@id="item3121016"]/div/div[2]/div[5]/text()[1]

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',charset='utf8')
cursor = conn.cursor()  # 创建游标，用于与数据库交互
#cursor.execute('drop database if exists article1')  # execute为执行SQL语句，此处的含义是如果存在数据库"test"，就把该数据库删掉
#cursor.execute('create database if not exists article1 character set utf8mb4 collate utf8mb4_general_ci')  # 如果不存在test数据库，则创建
conn.commit()  # commit()函数为手动提交对于数据库的修改

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')

cursor = conn.cursor() 
cursor.execute('CREATE TABLE `xiabnyaMovie` (`id` int NOT NULL,                `name` varchar(200) DEFAULT NULL,               `director` varchar(1000) DEFAULT NULL,               `description` varchar(10000) DEFAULT NULL,                `type` varchar(250) NOT NULL,                `pic` varchar(200) DEFAULT NULL,       PRIMARY KEY (`id`)          ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4')
conn.commit()

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')


cursor = conn.cursor()
idIndex=0
i=0
#url cover title director intro
while(i<len(nameAtitleAdirAtype[0])):
    
    try:
        cursor.execute('INSERT INTO xiabnyaMovie  (id,name,director,description,type,pic)       VALUES (%s,%s,%s,%s,%s,%s)' ,(i,nameAtitleAdirAtype[1][i],nameAtitleAdirAtype[2][i],nameAtitleAdirAtype[5][i],nameAtitleAdirAtype[3][i],nameAtitleAdirAtype[0][i]))
        print("make"+str(idIndex))
        idIndex+=1
        i=i+1
    except:
        idIndex+=1
        i=i+1
   
print("done")
conn.commit()

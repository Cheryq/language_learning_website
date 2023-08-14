from lxml import etree
import pymysql
from pymysql import apilevel
import requests
list=['https://mandarincompanion.com/blog/improve-your-listening-skills-step-1-know-the-challenges/', 'https://mandarincompanion.com/blog/how-to-read-chinese-in-4-steps-a-guide-for-beginners/', 'https://mandarincompanion.com/blog/chinese-reading-exercises/', 'https://mandarincompanion.com/blog/chinese-tutor/', 'https://mandarincompanion.com/blog/teach-yourself-mandarin/', 'https://mandarincompanion.com/blog/motivation-to-learn-chinese/', 'https://mandarincompanion.com/blog/chinese-reading-for-beginners/', 'https://mandarincompanion.com/blog/new-book-just-friends-breakthrough-level/', 'https://mandarincompanion.com/blog/new-breakthrough-story-in-search-of-hua-ma/', 'https://mandarincompanion.com/blog/new-breakthrough-story-my-teacher-is-a-martian/', 'https://mandarincompanion.com/blog/interview-with-steven-kaufmann-the-linguist/', 'https://mandarincompanion.com/blog/audiobooks-are-here/', 'https://mandarincompanion.com/blog/launch-of-the-new-breakthrough-level-books-150-characters/', 'https://mandarincompanion.com/blog/how-to-pass-the-ap-chinese-exam-secrets-from-a-teacher-with-a-perfect-pass-rate/', 'https://mandarincompanion.com/blog/stories-from-our-readers-from-flash-cards-to-martial-arts-jonathans-story/', 'https://mandarincompanion.com/blog/announcing-the-launch-of-our-podcast/', 'https://mandarincompanion.com/blog/mandarin-companion-preview-for-2019/', 'https://mandarincompanion.com/blog/emma-the-prince-and-the-pauper-and-the-ransom-of-red-chief-now-available-on-kindle/', 'https://mandarincompanion.com/blog/stories-from-our-readers-i-couldnt-believe-i-could-read-harriets-story/', 'https://mandarincompanion.com/blog/what-if-beginning-level-chinese-books-are-too-hard-10-tips-for-beginning-readers/', 'https://mandarincompanion.com/blog/stories-from-our-readers-chinese-is-like-an-elephant/', 'https://mandarincompanion.com/blog/why-we-forget/', 'https://mandarincompanion.com/blog/pinyin-over-characters-the-crippling-crutch/', 'https://mandarincompanion.com/blog/dont-be-so-serious-finally-a-funny-level-1-story/', 'https://mandarincompanion.com/blog/independent-study-confirms-the-readability-of-the-mandarin-companion-series/', 'https://mandarincompanion.com/blog/confessions-of-a-chinese-immigrant/', 'https://mandarincompanion.com/blog/jane-austens-emma/', 'https://mandarincompanion.com/blog/new-cooperation-between-chinesepod-and-mandarin-companion/', 'https://mandarincompanion.com/blog/the-prince-and-the-pauper-level-1-graded-reader/', 'https://mandarincompanion.com/blog/all-traditional-character-editions-available-in-paperback/', 'https://mandarincompanion.com/blog/journey-to-the-center-of-the-earth-illustration-adaptations/', 'https://mandarincompanion.com/blog/level-2-traditional-chinese-character-editions-on-sale/', 'https://mandarincompanion.com/blog/mandarin-companion-word-lists-now-available/', 'https://mandarincompanion.com/blog/the-magic-of-learning-from-context/', 'https://mandarincompanion.com/blog/level-2-is-here/', 'https://mandarincompanion.com/blog/will-reading-chinese-poems-improve-my-chinese/', 'https://mandarincompanion.com/blog/mandarin-companion-series-now-available-in-paperback/', 'https://mandarincompanion.com/blog/how-to-fix-your-e-reader-chinese-font-display-problems/', 'https://mandarincompanion.com/blog/the-secret-garden-in-paperback-and-level-2-update/', 'https://mandarincompanion.com/blog/how-great-are-your-expectations-level-2-in-progress/', 'https://mandarincompanion.com/blog/i-cant-learn-chinese-its-too-hard/', 'https://mandarincompanion.com/blog/the-impact-of-reading-results-of-a-40-year-study/', 'https://mandarincompanion.com/blog/the-only-way-we-truly-acquire-a-language/', 'https://mandarincompanion.com/blog/the-vicious-cycle-of-the-poor-reader/', 'https://mandarincompanion.com/blog/is-this-book-a-graded-reade/', 'https://mandarincompanion.com/blog/elementary-my-dear-watson-how-we-adapted-a-classic-to-chinese/', 'https://mandarincompanion.com/blog/activities-to-get-the-most-out-of-your-books/', 'https://mandarincompanion.com/blog/7-mistakes-about-extensive-reading/', 'https://mandarincompanion.com/blog/tales-from-readers-the-most-interesting-man-in-the-world/', 'https://mandarincompanion.com/blog/mandarin-companion-now-on-skritter/', 'https://mandarincompanion.com/blog/the-monkeys-paw-how-gruesome-should-it-be/', 'https://mandarincompanion.com/blog/reading-pain-or-reading-gain-reading-at-the-right-level/', 'https://mandarincompanion.com/blog/how-reading-in-chinese-changed-my-life/', 'https://mandarincompanion.com/blog/fateful-beginnings/', 'https://mandarincompanion.com/blog/welcome-to-mandarin-companion/']
def get_content(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    response=requests.get(url,headers=headers)
    response.encoding='utf-8'
    #print(response.text)
    tree=etree.HTML(response.text)
    title=tree.xpath('//meta[@property="og:title"]/@content')
    print(title)
    res=tree.xpath('//section[@class="post_content"]/p//text()')
    for i in range(0,len(res)):
        if(len(res[i])<10):
            if(i-1>=0):
                res[i-1]+=res[i]
                res[i]=""
            if(i+1<len(res)):
                res[i-1]+=res[i+1]
                res[i+1]=""
    for i in range(0,len(res)):
        if(res[i]!=""):
            print(res[i])
    allRes=[]
    allRes.append(title[0])
    allRes.append(res[0])
    for i in range(1,len(res)):
        if(res[i]!=""):
            allRes[1]=allRes[1]+"\n"+res[i]
            print(res[i])
    print(allRes[1])    
    return allRes
allContent=[]
for i in range(len(list)):
    allContent.append(get_content(list[i]))
    print("get"+str(i))


conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',charset='utf8')
cursor = conn.cursor()  # 创建游标，用于与数据库交互
cursor.execute('drop database if exists article1')  # execute为执行SQL语句，此处的含义是如果存在数据库"test"，就把该数据库删掉
cursor.execute('create database if not exists article1 character set utf8mb4 collate utf8mb4_general_ci')  # 如果不存在test数据库，则创建
conn.commit()  # commit()函数为手动提交对于数据库的修改

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')

cursor = conn.cursor() 
cursor.execute('CREATE TABLE `articleWeb2` (`id` varchar(100) NOT NULL,                `name` varchar(200) DEFAULT NULL,               `description` varchar(10000) DEFAULT NULL,       PRIMARY KEY (`id`),               UNIQUE KEY `name` (`name`) USING BTREE          ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4')
conn.commit()

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')


cursor = conn.cursor()
for i in range(len(allContent)):
    try:
        cursor.execute('INSERT INTO articleWeb2 (id,name, description)       VALUES (%s,%s, %s)' ,(str(i),allContent[i][0],allContent[i][1]))
        print("make"+str(i))
    except:
        continue
print("done")
conn.commit()
# -*- coding: UTF-8 -*-
url='https://movie.douban.com/tag/#/?sort=U&range=0,10&tags=%E6%97%A5%E6%9C%AC'
from collections import UserList
import requests
import pymysql
import json
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
    #director=tree.xpath('//span[@class="attrs"]/a/text()')
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
        
#get_content('https://movie.douban.com/subject/1291561/')

def get_url(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'}
    getQuery={'sort': 'U',
            'range':'0,10',
            'tags': '',
                'start': '0',
            'countries': '俄罗斯' }
    response=requests.get(url,headers=headers,data=getQuery)
    #print(response.content)
    jdata=json.loads(response.content)
    
    #print(jdata)
    
    print(type(jdata))
    urlAndCoverAndTitle=[]
    allUrl=[]
    allCover=[]
    allTitle=[]
    allDir=[]
    for i in range(0,20):
        allDir.append(jdata['data'][i]['directors'][0])
        allTitle.append(jdata['data'][i]['title'])
        allUrl.append(jdata['data'][i]['url'])
        allCover.append(jdata['data'][i]['cover'])
    urlAndCoverAndTitle.append(allUrl)
    urlAndCoverAndTitle.append(allCover)
    urlAndCoverAndTitle.append(allTitle)
    urlAndCoverAndTitle.append(allDir)
    print(urlAndCoverAndTitle)
    return urlAndCoverAndTitle
    #response.encoding='utf-8'
    #tree=etree.HTML(response.text)
    #print(response.text)
    #content=tree.xpath('//a[@ class="item"]/@href')
    #print(content)
    


url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0&countries=%E4%BF%84%E7%BD%97%E6%96%AF'

def main(url):
    urlAndCoverAndTitle=get_url(url)
    allIntro=[]
    for i in range(0,len(urlAndCoverAndTitle[0])):
        
        allIntro.append(get_content(urlAndCoverAndTitle[0][i]))
    urlAndCoverAndTitle.append(allIntro)
    print(urlAndCoverAndTitle)
    print(len(urlAndCoverAndTitle[0]))
    print(len(urlAndCoverAndTitle[1]))
    print(len(urlAndCoverAndTitle[2]))
    print(len(urlAndCoverAndTitle[3]))
    print(len(urlAndCoverAndTitle[4]))    
    #url cover title director intro
    return urlAndCoverAndTitle
#allContent=main(url)
  
    #print(strRes)
    #print(content)
#get_description('https://book.douban.com/subject/35143790/')


allPic=['https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2325999177.webp',
'https://img2.doubanio.com/view/subject/l/public/s6984421.jpg',
'https://img2.doubanio.com/view/photo/s_ratio_poster/public/p1650155363.webp',
'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2070139798.webp',
'https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2378459266.webp',
'https://img1.doubanio.com/view/subject/l/public/s1634899.jpg']
allTitle=['恐怖主义与烤肉 Al-irhab wal kabab',
'伟大的中国蚕豆',
'上帝的使者',
'欧麦尔',
'蕾娜的婚礼 Al qods fee yom akhar',
' 加里里的婚礼 Urs al-jalil']
allDirector=['Sherif Arafa','谢里夫·阿拉法赫','穆斯塔法·阿卡德','Hatem Ali',
'Hany Abu-Assad',
 'Michel Khleifi']
allType=['喜剧 / 犯罪','喜剧','剧情 / 传记 / 历史 / 战争',
'剧情 / 传记 / 历史','剧情 / 喜剧','剧情']
allIntro=['一个家庭成员被埃及公共系统的官僚主义和生活困难所挫败，他发现自己无意中被指控为恐怖主义分子，并决定继续在埃及最拥挤的公共服务大楼中扣押人质。一位敌对的内政部长作为一些同情和加入他的事业的人，目的是缓和局势。一个名叫艾哈迈德的人几天来一直试图去政府大楼完成必要的文书工作，把他的孩子转到另一所学校。他一再地看不到他需要会见的雇员。有人告诉他雇员有一次休假。另一次他被告知雇员在厕所里。他在大厅里遇到一个擦鞋人，他告诉他这个特别的雇员喜欢去更豪华的地方上厕所，所以艾哈迈德在幽默的场景中离开了政府大楼去找这个雇员。他必须回到政府大楼去寻找这个人，因为他的老板经常对他不满意。有一天，他在办公室里制造了一场骚乱，大楼的警卫被叫来对付他。在一场跟随艾哈迈德的混战中，艾哈迈德获得了警卫的武器，并意外地在政府大楼劫持了人质。大楼的所有其他楼层都疏散了，军队和内政部长被召唤；政府将艾哈迈德视为恐怖分子。艾哈迈德和人质要求政府提供烤肉串作为午餐。艾哈迈德实际上没有官方要求，只有正义。他想被当作人来对待。在向人质解释了这一点之后，人质决定喜欢艾哈迈德。他帮助他们中的一些人得到他们需要的东西；他告诉警方，他要求为其中一名人质提供药物治疗。最后，他们一起走出了大楼，而政府也不知道谁是恐怖分子.',
'如果您在公元两千零四年之后徜徉在开罗街头，漫步于集市的喧嚷并在清真寺的阴影里享受片刻凉爽，不出片刻就会有几个礼貌欠妥的半大孩子围住你搭讪。通常他们会说 妮袄 ，你回答“你好”。然后他们会毫无理由地说 卜咬，卜咬 ——有时还会越说越来劲，从街巷的各个角落里冒出好几十个小孩子将“卜咬”汇成一股巨大的声浪把你掀倒。',
'加麦，七世纪，穆罕默德与城市的强权者们斗争着，他揭露他们的专横，以及它造成的疾病－奴隶制，暴力，酗酒，特别是，穆罕默德和他的信徒们鼓励人们忘却旧偶像，只崇拜唯一的真主，他们的对手毫不犹豫的迫害并折磨他们的近亲。然而，和平的穆斯林们明白，该为尊重自己的正义而奋战…',
"Farouk Omar is a historical Arab series co-produced by MBC1 and Qatar TV and directed by Hatem Ali, which is based on one of the best companions of Prophet Muhammad (Peace be upon him) and the 2nd Caliph of the Islamic state, Umar Ibn Al-Khattab (May Allah be pleased with him) . A 30-episode series showcasing the various events during the life of Umar Ibn Al-Khattab (May Allah be pleased with him) from his pre-Islamic days till his assassination. The series depends solely on established historical facts hence didn't face criticism in terms of its content as past movies on similar subjects did. The series commences with the 23 year of Hijra at Makkah, where the Muslim pilgrims have come together for the Hajj. In midst of them, we can see Umar Ibn Al Khattab (May Allah be pleased with him) supplicating to the Lord while doing the Tawaaf around the Ka'abah. On the return journey to Medinah from Makkah, they pass by a group of people tending to their camels in the desert. Umar (May Allah be pleased with him) reminisces his past days, when he used to tend to his father Al-Khattab's camels in the desert, and how his father used to work him to exhaustion and beat him up if he slackened. However, now after his embracing Islam how life has changed for him with no one to stand between him and his Lord. The series then takes you on a historical ride as memories come gushing back to Umar (May Allah be pleased with him) about the various events that happened during his lifetime.",
"About a Palestinian girl of 17 who wants to get married to the man of her own choosing. Rana wakes up one morning to an ultimatum delivered by her father: she must either choose a husband from a preselected list of men, or she must leave Palestine for Egypt with her father by 4:00 that afternoon. With ten hours to find her boyfriend in occupied Jerusalem, she sneaks out of her father's house at daybreak to find her forbidden love Khalil (Natour).",
"本片其实是借着双方的首领，来隐喻上帝和阿拉之间亘古的宗教冲突，一方是拥有军权的指挥官，一方是拥有家族势力的村长，双方都想主宰命运，但胜利却属于..."]
allContent=[]

allContent.append(allPic)
allContent.append(allTitle)
allContent.append(allDirector)
allContent.append(allType)
allContent.append(allIntro)

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',charset='utf8')
cursor = conn.cursor()  # 创建游标，用于与数据库交互
#cursor.execute('drop database if exists article1')  # execute为执行SQL语句，此处的含义是如果存在数据库"test"，就把该数据库删掉
#cursor.execute('create database if not exists article1 character set utf8mb4 collate utf8mb4_general_ci')  # 如果不存在test数据库，则创建
conn.commit()  # commit()函数为手动提交对于数据库的修改

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')

cursor = conn.cursor() 
cursor.execute('CREATE TABLE `alaboMovie` (`id` int NOT NULL,                `name` varchar(200) DEFAULT NULL,               `director` varchar(1000) DEFAULT NULL,               `description` varchar(10000) DEFAULT NULL,                `type` varchar(250) NOT NULL,                `pic` varchar(200) DEFAULT NULL,       PRIMARY KEY (`id`)          ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4')
conn.commit()

conn=pymysql.connect(host='localhost',port=3306,user='root',password='Teng0205',db='article1',charset='utf8')


cursor = conn.cursor()
idIndex=0
i=0
#url cover title director intro
while(i<len(allContent[0])):
    
    try:
        cursor.execute('INSERT INTO alaboMovie (id,name,director,description,type,pic)       VALUES (%s,%s,%s,%s,%s,%s)' ,(i,allContent[1][i],allContent[2][i],allContent[4][i],allContent[3][i],allContent[0][i]))
        print("make"+str(idIndex))
        idIndex+=1
        i=i+1
    except:
        idIndex+=1
        i=i+1
   
print("done")
conn.commit()

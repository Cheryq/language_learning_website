import pymysql


# class1=FetchData(baseName)   getArticle() 得到文章名字的列表   getWords()得到单词+翻译的列表  形如【‘int','整形’，‘string','字符串’】

# class2=InsertData(baseName)       insertWords(word,translation)    insertArticle(articleName)
class FetchData(object):
    def __init__(self, name):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password="20010126mzq", database=name,
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def getArticle(self):
        sql = " select* from article"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.conn.commit()
        # print(type(results))
        # print(results)
        res = []
        for i in range(0, len(results)):
            res.append(results[i][0])
        print(res)
        return res

    def getWords(self):
        sql = " select* from words"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.conn.commit()
        # print(results)
        res = []
        for i in range(0, len(results)):
            res.append(results[i])
        print(res)
        return res


# test
# object1=FetchData('2133')
# object1.getWords()
# object1.getArticle()

class InsertData(object):
    def __init__(self, name):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='20010126mzq', database=name,
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def insertWords(self, word, translation):
        try:
            self.cursor.execute('INSERT INTO words (name,translation)  VALUES(%s,%s)', (word, translation))
            # print("word wrong")
            self.conn.commit()
            print(1)
        except:
            print("word wrong")

    def insertArticle(self, articleName):
        try:
            self.cursor.execute('INSERT INTO article (name)       VALUES(%s)', (articleName))
            self.conn.commit()
        except:
            print("article wrong")
# object1=InsertData('2133')
# object1.insertArticle('articleTest4')
# object1.insertWords('wordsTest4','wordTranslation4')

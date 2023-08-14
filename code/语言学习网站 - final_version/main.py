import flask
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pymysql
import random
from fetchData import InsertData
from fetchData import FetchData

# 创建数据库
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='20010126mzq',
                       charset='utf8',
                       db="all_in_one")
cursor = conn.cursor()
Username = "guest"
url_pre = "http://localhost:5000/article/"
# 路由绑定
app = Flask(__name__)
CORS(app, resources=r'/')


@app.route('/language/en', methods=['POST', 'GET'])
def fetch_en():
    username_tmp = request.args.get('username', '')
    word_get = request.args.get('word', '')
    translation_get = request.args.get('tra', '')
    global Username
    if username_tmp != '':
        Username = username_tmp
    if word_get != '':
        class_user = InsertData(Username)
        class_user.insertWords(word_get, translation_get)
    word = [''] * 674
    pro = [''] * 674
    tra = [''] * 674
    for i in range(300):
        sql = 'SELECT * FROM 英语单词 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        Id = i
        if result is None:
            word[i] = "NULL"
            pro[i] = "NULL"
            tra[i] = "NULL"
        else:
            word[i] = result[1]
            pro[i] = result[2]
            tra[i] = result[3]
    cursor.execute('SELECT * FROM `英语书`')
    book_data = random.sample(list(cursor.fetchall()), 5)
    cursor.execute('SELECT * FROM `英语文章`')
    article_data = random.sample(list(cursor.fetchall()), 3)
    cursor.execute('SELECT * FROM `英语电影`')
    video_data = list(cursor.fetchall())[:6]
    for i in range(5):
        book_data[i] = list(book_data[i])
        book_data[i][4] = "https://images.weserv.nl/?url=" + book_data[i][4]
    for j in range(6):
        video_data[j] = list(video_data[j])
        video_data[j][4] = "https://images.weserv.nl/?url=" + video_data[j][4]
    fetch_user = FetchData(Username)
    users_data = fetch_user.getWords()
    print(users_data)
    return render_template("language.html", book_data=book_data, language="英语", article_data=article_data,
                           video_data=video_data, ten=[i for i in range(1, 300)], num=[i for i in range(2, 300)],
                           word=word,
                           pro=pro, tra=tra, users_data=users_data, user_name=Username, more_article=url_pre + "en")


@app.route('/language/jp', methods=['POST', 'GET'])
def fetch_jp():
    username_tmp = request.args.get('username', '')
    word_get = request.args.get('word', '')
    translation_get = request.args.get('tra', '')
    global Username
    if username_tmp != '':
        Username = username_tmp
    if word_get != '':
        class_user = InsertData(Username)
        class_user.insertWords(word_get, translation_get)
    word = [''] * 674
    pro = [''] * 674
    tra = [''] * 674
    for i in range(300):
        sql = 'SELECT * FROM 日语单词 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        Id = i
        if result is None:
            word[i] = "NULL"
            pro[i] = "NULL"
            tra[i] = "NULL"
        else:
            word[i] = result[1]
            pro[i] = result[2]
            tra[i] = result[3]
    cursor.execute('SELECT * FROM `日语书`')
    book_data = random.sample(list(cursor.fetchall()), 5)
    cursor.execute('SELECT * FROM `日语文章`')
    article_data = random.sample(list(cursor.fetchall()), 3)
    cursor.execute('SELECT * FROM `日语电影`')
    video_data = list(cursor.fetchall())[:6]
    for i in range(5):
        book_data[i] = list(book_data[i])
        book_data[i][4] = "https://images.weserv.nl/?url=" + book_data[i][4]
    for j in range(6):
        video_data[j] = list(video_data[j])
        video_data[j][4] = "https://images.weserv.nl/?url=" + video_data[j][4]
    fetch_user = FetchData(Username)
    users_data = fetch_user.getWords()
    print(users_data)
    return render_template("language.html", book_data=book_data, language="日语", article_data=article_data,
                           video_data=video_data, ten=[i for i in range(1, 300)], num=[i for i in range(2, 300)],
                           word=word,
                           pro=pro, tra=tra, users_data=users_data, user_name=Username, more_article=url_pre + "jp")


@app.route('/language/it', methods=['POST', 'GET'])
def fetch_it():
    username_tmp = request.args.get('username', '')
    word_get = request.args.get('word', '')
    translation_get = request.args.get('tra', '')
    global Username
    if username_tmp != '':
        Username = username_tmp
    if word_get != '':
        class_user = InsertData(Username)
        class_user.insertWords(word_get, translation_get)
    word = [''] * 674
    pro = [''] * 674
    tra = [''] * 674
    for i in range(300):
        sql = 'SELECT * FROM 意大利语单词 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        Id = i
        if result is None:
            word[i] = "NULL"
            pro[i] = "NULL"
            tra[i] = "NULL"
        else:
            word[i] = result[1]
            pro[i] = result[2]
            tra[i] = result[3]
    cursor.execute('SELECT * FROM `意大利语书`')
    book_data = random.sample(list(cursor.fetchall()), 5)
    cursor.execute('SELECT * FROM `意大利语文章`')
    article_data = random.sample(list(cursor.fetchall()), 3)
    cursor.execute('SELECT * FROM `意大利语电影`')
    video_data = list(cursor.fetchall())[:6]
    for i in range(5):
        book_data[i] = list(book_data[i])
        book_data[i][4] = "https://images.weserv.nl/?url=" + book_data[i][4]
    for j in range(6):
        video_data[j] = list(video_data[j])
        video_data[j][4] = "https://images.weserv.nl/?url=" + video_data[j][4]
    fetch_user = FetchData(Username)
    users_data = fetch_user.getWords()
    print(users_data)
    return render_template("language.html", book_data=book_data, language="意大利语", article_data=article_data,
                           video_data=video_data, ten=[i for i in range(1, 300)], num=[i for i in range(2, 300)],
                           word=word,
                           pro=pro, tra=tra, users_data=users_data, user_name=Username, more_article=url_pre + "it")


@app.route('/language/sp', methods=['POST', 'GET'])
def fetch_sp():
    username_tmp = request.args.get('username', '')
    word_get = request.args.get('word', '')
    translation_get = request.args.get('tra', '')
    global Username
    if username_tmp != '':
        Username = username_tmp
    if word_get != '':
        class_user = InsertData(Username)
        class_user.insertWords(word_get, translation_get)
    word = [''] * 674
    pro = [''] * 674
    tra = [''] * 674
    for i in range(300):
        sql = 'SELECT * FROM 西班牙语单词 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        Id = i
        if result is None:
            word[i] = "NULL"
            pro[i] = "NULL"
            tra[i] = "NULL"
        else:
            word[i] = result[1]
            pro[i] = result[2]
            tra[i] = result[3]
    cursor.execute('SELECT * FROM `西班牙语书`')
    book_data = random.sample(list(cursor.fetchall()), 5)
    cursor.execute('SELECT * FROM `西班牙语文章`')
    article_data = random.sample(list(cursor.fetchall()), 3)
    cursor.execute('SELECT * FROM `西班牙语电影`')
    video_data = list(cursor.fetchall())[:6]
    for i in range(5):
        book_data[i] = list(book_data[i])
        book_data[i][4] = "https://images.weserv.nl/?url=" + book_data[i][4]
    for j in range(6):
        video_data[j] = list(video_data[j])
        video_data[j][4] = "https://images.weserv.nl/?url=" + video_data[j][4]
    fetch_user = FetchData(Username)
    users_data = fetch_user.getWords()
    print(users_data)
    return render_template("language.html", book_data=book_data, language="西班牙语", article_data=article_data,
                           video_data=video_data, ten=[i for i in range(1, 300)], num=[i for i in range(2, 300)],
                           word=word,
                           pro=pro, tra=tra, users_data=users_data, user_name=Username, more_article=url_pre + "sp")


@app.route('/language/pt', methods=['POST', 'GET'])
def fetch_pt():
    username_tmp = request.args.get('username', '')
    word_get = request.args.get('word', '')
    translation_get = request.args.get('tra', '')
    global Username
    if username_tmp != '':
        Username = username_tmp
    if word_get != '':
        class_user = InsertData(Username)
        class_user.insertWords(word_get, translation_get)
    word = [''] * 674
    pro = [''] * 674
    tra = [''] * 674
    for i in range(300):
        sql = 'SELECT * FROM 葡萄牙语单词 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        Id = i
        if result is None:
            word[i] = "NULL"
            pro[i] = "NULL"
            tra[i] = "NULL"
        else:
            word[i] = result[1]
            pro[i] = result[2]
            tra[i] = result[3]
    cursor.execute('SELECT * FROM `葡萄牙语书`')
    book_data = random.sample(list(cursor.fetchall()), 5)
    cursor.execute('SELECT * FROM `葡萄牙语文章`')
    article_data = random.sample(list(cursor.fetchall()), 3)
    cursor.execute('SELECT * FROM `葡萄牙语电影`')
    video_data = list(cursor.fetchall())[:6]
    for i in range(5):
        book_data[i] = list(book_data[i])
        book_data[i][4] = "https://images.weserv.nl/?url=" + book_data[i][4]
    for j in range(6):
        video_data[j] = list(video_data[j])
        video_data[j][4] = "https://images.weserv.nl/?url=" + video_data[j][4]
    fetch_user = FetchData(Username)
    users_data = fetch_user.getWords()
    print(users_data)
    return render_template("language.html", book_data=book_data, language="葡萄牙语", article_data=article_data,
                           video_data=video_data, ten=[i for i in range(1, 300)], num=[i for i in range(2, 300)],
                           word=word,
                           pro=pro, tra=tra, users_data=users_data, user_name=Username, more_article=url_pre + "pt")


@app.route('/language/ko', methods=['POST', 'GET'])
def fetch_ko():
    username_tmp = request.args.get('username', '')
    word_get = request.args.get('word', '')
    translation_get = request.args.get('tra', '')
    global Username
    if username_tmp != '':
        Username = username_tmp
    if word_get != '':
        class_user = InsertData(Username)
        class_user.insertWords(word_get, translation_get)
    word = [''] * 674
    pro = [''] * 674
    tra = [''] * 674
    for i in range(300):
        sql = 'SELECT * FROM 韩语单词 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        Id = i
        if result is None:
            word[i] = "NULL"
            pro[i] = "NULL"
            tra[i] = "NULL"
        else:
            word[i] = result[1]
            pro[i] = result[2]
            tra[i] = result[3]
    cursor.execute('SELECT * FROM `韩语书`')
    book_data = random.sample(list(cursor.fetchall()), 5)
    cursor.execute('SELECT * FROM `韩语文章`')
    article_data = random.sample(list(cursor.fetchall()), 3)
    cursor.execute('SELECT * FROM `韩语电影`')
    video_data = list(cursor.fetchall())[:6]
    for i in range(5):
        book_data[i] = list(book_data[i])
        book_data[i][4] = "https://images.weserv.nl/?url=" + book_data[i][4]
    for j in range(6):
        video_data[j] = list(video_data[j])
        video_data[j][4] = "https://images.weserv.nl/?url=" + video_data[j][4]
    fetch_user = FetchData(Username)
    users_data = fetch_user.getWords()
    print(users_data)
    return render_template("language.html", book_data=book_data, language="韩语", article_data=article_data,
                           video_data=video_data, ten=[i for i in range(1, 300)], num=[i for i in range(2, 300)],
                           word=word,
                           pro=pro, tra=tra, users_data=users_data, user_name=Username, more_article=url_pre + "ko")


@app.route('/language/fr', methods=['POST', 'GET'])
def fetch_fr():
    username_tmp = request.args.get('username', '')
    word_get = request.args.get('word', '')
    translation_get = request.args.get('tra', '')
    global Username
    if username_tmp != '':
        Username = username_tmp
    if word_get != '':
        class_user = InsertData(Username)
        class_user.insertWords(word_get, translation_get)
    word = [''] * 674
    pro = [''] * 674
    tra = [''] * 674
    for i in range(300):
        sql = 'SELECT * FROM 法语单词 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        Id = i
        if result is None:
            word[i] = "NULL"
            pro[i] = "NULL"
            tra[i] = "NULL"
        else:
            word[i] = result[1]
            pro[i] = result[2]
            tra[i] = result[3]
    cursor.execute('SELECT * FROM `法语书`')
    book_data = random.sample(list(cursor.fetchall()), 5)
    cursor.execute('SELECT * FROM `法语文章`')
    article_data = random.sample(list(cursor.fetchall()), 3)
    cursor.execute('SELECT * FROM `法语电影`')
    video_data = list(cursor.fetchall())[:6]
    for i in range(5):
        book_data[i] = list(book_data[i])
        book_data[i][4] = "https://images.weserv.nl/?url=" + book_data[i][4]
    for j in range(6):
        video_data[j] = list(video_data[j])
        video_data[j][4] = "https://images.weserv.nl/?url=" + video_data[j][4]
    fetch_user = FetchData(Username)
    users_data = fetch_user.getWords()
    print(users_data)
    return render_template("language.html", book_data=book_data, language="法语", article_data=article_data,
                           video_data=video_data, ten=[i for i in range(1, 300)], num=[i for i in range(2, 300)],
                           word=word,
                           pro=pro, tra=tra, users_data=users_data, user_name=Username, more_article=url_pre + "fr")


@app.route('/language/ru', methods=['POST', 'GET'])
def fetch_ru():
    username_tmp = request.args.get('username', '')
    word_get = request.args.get('word', '')
    translation_get = request.args.get('tra', '')
    global Username
    if username_tmp != '':
        Username = username_tmp
    if word_get != '':
        class_user = InsertData(Username)
        class_user.insertWords(word_get, translation_get)
    word = [''] * 674
    pro = [''] * 674
    tra = [''] * 674
    for i in range(300):
        sql = 'SELECT * FROM 俄语单词 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        Id = i
        if result is None:
            word[i] = "NULL"
            pro[i] = "NULL"
            tra[i] = "NULL"
        else:
            word[i] = result[1]
            pro[i] = result[2]
            tra[i] = result[3]
    cursor.execute('SELECT * FROM `俄语书`')
    book_data = random.sample(list(cursor.fetchall()), 5)
    cursor.execute('SELECT * FROM `俄语文章`')
    article_data = random.sample(list(cursor.fetchall()), 3)
    cursor.execute('SELECT * FROM `俄语电影`')
    video_data = list(cursor.fetchall())[:6]
    for i in range(5):
        book_data[i] = list(book_data[i])
        book_data[i][4] = "https://images.weserv.nl/?url=" + book_data[i][4]
    for j in range(6):
        video_data[j] = list(video_data[j])
        video_data[j][4] = "https://images.weserv.nl/?url=" + video_data[j][4]
    fetch_user = FetchData(Username)
    users_data = fetch_user.getWords()
    print(users_data)
    return render_template("language.html", book_data=book_data, language="俄语", article_data=article_data,
                           video_data=video_data, ten=[i for i in range(1, 300)], num=[i for i in range(2, 300)],
                           word=word,
                           pro=pro, tra=tra, users_data=users_data, user_name=Username, more_article=url_pre + "ru")


@app.route('/language/ge', methods=['POST', 'GET'])
def fetch_ge():
    username_tmp = request.args.get('username', '')
    word_get = request.args.get('word', '')
    translation_get = request.args.get('tra', '')
    global Username
    if username_tmp != '':
        Username = username_tmp
    if word_get != '':
        class_user = InsertData(Username)
        class_user.insertWords(word_get, translation_get)
    word = [''] * 674
    pro = [''] * 674
    tra = [''] * 674
    for i in range(300):
        sql = 'SELECT * FROM 德语单词 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        Id = i
        if result is None:
            word[i] = "NULL"
            pro[i] = "NULL"
            tra[i] = "NULL"
        else:
            word[i] = result[1]
            pro[i] = result[2]
            tra[i] = result[3]
    cursor.execute('SELECT * FROM `德语书`')
    book_data = random.sample(list(cursor.fetchall()), 5)
    cursor.execute('SELECT * FROM `德语文章`')
    article_data = random.sample(list(cursor.fetchall()), 3)
    cursor.execute('SELECT * FROM `德语电影`')
    video_data = list(cursor.fetchall())[:6]
    for i in range(5):
        book_data[i] = list(book_data[i])
        book_data[i][4] = "https://images.weserv.nl/?url=" + book_data[i][4]
    for j in range(6):
        video_data[j] = list(video_data[j])
        video_data[j][4] = "https://images.weserv.nl/?url=" + video_data[j][4]
    fetch_user = FetchData(Username)
    users_data = fetch_user.getWords()
    print(users_data)
    return render_template("language.html", book_data=book_data, language="德语", article_data=article_data,
                           video_data=video_data, ten=[i for i in range(1, 300)], num=[i for i in range(2, 300)], word=word,
                           pro=pro, tra=tra, users_data=users_data, user_name=Username, more_article=url_pre + "ge")


@app.route('/language/al', methods=['POST', 'GET'])
def fetch_al():
    username_tmp = request.args.get('username', '')
    word_get = request.args.get('word', '')
    translation_get = request.args.get('tra', '')
    global Username
    if username_tmp != '':
        Username = username_tmp
    if word_get != '':
        class_user = InsertData(Username)
        class_user.insertWords(word_get, translation_get)
    word = [''] * 674
    pro = [''] * 674
    tra = [''] * 674
    for i in range(300):
        sql = 'SELECT * FROM 阿拉伯语单词 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        Id = i
        if result is None:
            word[i] = "NULL"
            pro[i] = "NULL"
            tra[i] = "NULL"
        else:
            word[i] = result[1]
            pro[i] = result[2]
            tra[i] = result[3]
    cursor.execute('SELECT * FROM `阿拉伯语书`')
    book_data = random.sample(list(cursor.fetchall()), 5)
    cursor.execute('SELECT * FROM `阿拉伯语文章`')
    article_data = random.sample(list(cursor.fetchall()), 3)
    cursor.execute('SELECT * FROM `阿拉伯语电影`')
    video_data = list(cursor.fetchall())[:6]
    for i in range(5):
        book_data[i] = list(book_data[i])
        book_data[i][4] = "https://images.weserv.nl/?url=" + book_data[i][4]
    for j in range(6):
        video_data[j] = list(video_data[j])
        video_data[j][4] = "https://images.weserv.nl/?url=" + video_data[j][4]
    fetch_user = FetchData(Username)
    users_data = fetch_user.getWords()
    print(users_data)
    return render_template("language.html", book_data=book_data, language="阿拉伯语", article_data=article_data,
                           video_data=video_data, ten=[i for i in range(1, 300)], num=[i for i in range(2, 300)], word=word,
                           pro=pro, tra=tra, users_data=users_data, user_name=Username, more_article=url_pre + "al")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8899)

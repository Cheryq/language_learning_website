import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)
conn = pymysql.connect(user='root', host='localhost', port=3306, passwd='20010126mzq', db='all_in_one')
cursor = conn.cursor()
name = [' '] * 10
assay = [' '] * 10


@app.route('/article/al')
def test1():
    for i in range(1, 11):
        sql = 'SELECT * FROM 阿拉伯语文章 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        name[i - 1] = result[2]
        assay[i - 1] = result[1]
    return render_template('index.html', ten=[i for i in range(1, 11)], name=name, assay=assay)


@app.route('/article/en')
def test2():
    for i in range(1, 11):
        sql = 'SELECT * FROM 英语文章 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        name[i - 1] = result[2]
        assay[i - 1] = result[1]
    return render_template('index.html', ten=[i for i in range(1, 11)], name=name, assay=assay)


@app.route('/article/ko')
def test3():
    for i in range(1, 11):
        sql = 'SELECT * FROM 韩语文章 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        name[i - 1] = result[2]
        assay[i - 1] = result[1]
    return render_template('index.html', ten=[i for i in range(1, 11)], name=name, assay=assay)


@app.route('/article/jp')
def test4():
    for i in range(1, 11):
        sql = 'SELECT * FROM 日语文章 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        name[i - 1] = result[2]
        assay[i - 1] = result[1]
    return render_template('index.html', ten=[i for i in range(1, 11)], name=name, assay=assay)


@app.route('/article/ge')
def test5():
    for i in range(1, 11):
        sql = 'SELECT * FROM 德语文章 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        name[i - 1] = result[2]
        assay[i - 1] = result[1]
    return render_template('index.html', ten=[i for i in range(1, 11)], name=name, assay=assay)


@app.route('/article/fr')
def test6():
    for i in range(1, 11):
        sql = 'SELECT * FROM 法语文章 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        name[i - 1] = result[2]
        assay[i - 1] = result[1]
    return render_template('index.html', ten=[i for i in range(1, 11)], name=name, assay=assay)


@app.route('/article/sp')
def test7():
    for i in range(1, 11):
        sql = 'SELECT * FROM 西班牙语文章 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        name[i - 1] = result[2]
        assay[i - 1] = result[1]
    return render_template('index.html', ten=[i for i in range(1, 11)], name=name, assay=assay)


@app.route('/article/pt')
def test8():
    for i in range(1, 11):
        sql = 'SELECT * FROM 葡萄牙语文章 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        name[i - 1] = result[2]
        assay[i - 1] = result[1]
    return render_template('index.html', ten=[i for i in range(1, 11)], name=name, assay=assay)


@app.route('/article/ru')
def test9():
    for i in range(1, 11):
        sql = 'SELECT * FROM 俄语文章 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        name[i - 1] = result[2]
        assay[i - 1] = result[1]
    return render_template('index.html', ten=[i for i in range(1, 11)], name=name, assay=assay)


@app.route('/article/it')
def test10():
    for i in range(1, 11):
        sql = 'SELECT * FROM 意大利语文章 WHERE id="%s"'
        cursor.execute(sql % i)
        result = cursor.fetchone()
        name[i - 1] = result[2]
        assay[i - 1] = result[1]
    return render_template('index.html', ten=[i for i in range(1, 11)], name=name, assay=assay)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pymysql
import random

# 路由绑定
app = Flask(__name__)
CORS(app, resources=r'/')


@app.route('/homepage', methods=['POST', 'GET'])
def homepage():
    return render_template("index.html")


@app.route('/introduction', methods=['POST', 'GET'])
def introduction():
    return render_template("index_introduction.html")


@app.route('/member', methods=['POST', 'GET'])
def member():
    return render_template("index_member.html")


@app.route('/search', methods=['POST', 'GET'])
def language_search():
    conn2 = pymysql.connect(user='root', host='localhost', port=3306, passwd='20010126mzq', db='language_search')
    cur = conn2.cursor()
    S = request.args.get('name', '')
    sql = "select * from 文章搜索 where name like '%" + S + "%'"
    cur.execute(sql)
    datas = cur.fetchall()
    if S == '':
        items = "输入你想搜索的文章关键词"
    else:
        if datas == ():
            items = "没有搜索到"
        else:
            items = datas[0][1]
    return render_template('language_search.html', items=items)


@app.route('/map', methods=['POST', 'GET'])
def mapping():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8989)

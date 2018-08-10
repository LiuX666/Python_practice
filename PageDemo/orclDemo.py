#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cx_Oracle
from flask import Flask,jsonify,request,render_template
from flask_cors import *

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

users = [
    {'username': 'Tom', 'password': '123'},
    {'username': 'Mike', 'password': '123'}
]

@auth.get_password
def get_password(username):
    for user in users:
        if user['username'] == username:
            return user['password']
    return None

import os
os.environ["NLS_LANG"] = "SIMPLIFIED CHINESE_CHINA.UTF8"

app = Flask(__name__)
CORS(app, supports_credentials=True)

conn = cx_Oracle.connect('dev/dev@192.168.22.32/orcl')
curs = conn.cursor()

@app.route('/')
def index():
    return  render_template('index.html')


@app.route('/get')
@auth.login_required
def get_query():
    curs.execute("select * from STUDENT")
    rows = curs.fetchall()
    return jsonify(rows)


@app.route('/getone/<int:id>')
def get_queryone(id):
    curs.execute("select * from STUDENT where ID=%d"%id)
    row = curs.fetchone()
    return jsonify(row)

@app.route('/insert',methods=['POST'])
def insert_query():
    ids= request.json['id']
    sname=request.json['sname']
    age=request.json['age']
    sql="insert into STUDENT(ID,SNAME,AGE) values ('%s','%s','%s')" % (ids,sname,age)
    curs.execute(sql)
    conn.commit()
    return "添加成功"

@app.route('/delete/<int:id>')
def delete_query(id):
    sql="delete from STUDENT where id=%d"%id
    curs.execute(sql)
    conn.commit()
    return "删除成功"

@app.route('/update/<int:id>',methods=['POST'])
def update_query(id):
    ids = request.json['id']
    sname = request.json['sname']
    age = request.json['age']
    sql="update STUDENT set ID='%s',SNAME='%s',AGE='%s' where ID=%d"%(ids,sname,age,id)
    curs.execute(sql)
    conn.commit()
    return "更新成功"


if __name__ == '__main__':
    app.run()





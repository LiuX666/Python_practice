#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者：liux
日期：2018/6/25 15:39
功能：flask session例子
"""

from flask import Flask,session,request
app = Flask(__name__)

#第二步:获取session的值
@app.route('/s')
def hello_world():
    print(session.getlist('username'))
    print(session['username'])
    return 'app-Hello World!'

#第一步：session赋值
@app.route('/login')
def login():
    session['username'] = request.args.get('username')
    return '成功'

#注销session
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return '注销'


# @app.before_request
# def before_user():
#     print(request.remote_addr)
#     if 'username' in session:
#         return '已登录'
#         pass
#     else:
#         return '未登录'


# set the secret key.  keep this really secret
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
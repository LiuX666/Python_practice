#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者：liux
日期：2018/8/16 9:08
功能：flask cas 单点登录
"""
from flask import Flask,session,request
from PythonPractice.flask_cas import CAS
from PythonPractice.flask_cas import login_required
from PythonPractice.flask_cas import logout_required

app = Flask(__name__)

cas = CAS(app, '/cas')

app.config['CAS_SERVER'] = 'http://11111/cas/login?service=http://2222/loginout'
app.config['CAS_AFTER_LOGIN'] = 'route_root'

@app.route('/test')
@login_required
def login():
    username = cas.username
    print(username)
    # print(session['CAS_USERNAME'])
    return 'qqqqq'
    # display_name = cas.attributes['cas:displayName']


@app.route('/loginout')
def cleanSession():
    return 'qqqdq'

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LuWX/,?RT'


if __name__ == '__main__':
    app.run(host='0.0.0.0')


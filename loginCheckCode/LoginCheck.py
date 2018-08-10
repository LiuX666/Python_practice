#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者：liux
日期：2018/8/6 14:01
功能：验证图片记录在响应，验证码记在session中
"""
from flask import Flask,session,request,make_response

from io import BytesIO
from loginCheckCode.pyUtils.randomCheckCode import random_check_code

app = Flask(__name__)

@app.route('/loginImgCheck')
def checkLogin():
    img, code = random_check_code()
    #img.save('idencode.png')
    #img.show()
    stream = BytesIO()
    img.save(stream, 'png')
    session['code'] = code
    return make_response(stream.getvalue())

@app.route('/loginSession')
def getloginSession():
    codeS= session['code']
    return codeS

app.secret_key = 'A0Zr98j/3yX R~XggHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8550, threaded=True)

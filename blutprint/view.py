# -*- coding: UTF-8 -*-

from flask import Flask
from blutprint.admin import admin   # 从分路由倒入路由函数
from blutprint.user import user
import json

app = Flask(__name__)

 # 注册蓝图 第一个参数 是蓝图对象
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user,url_prefix='/user')


@app.route('/')
def hello_world():
   return 'app-Hello World!'

if __name__ == '__main__':
    app.run()
# -*- coding: UTF-8 -*-

from flask import Blueprint , render_template

#  创建蓝图 第二个参数为蓝图的名字
user = Blueprint('user',__name__)

@user.route('/user')
def user_demo():
   return 'user'
# -*- coding: UTF-8 -*-

from flask import Blueprint

#  创建蓝图 第一个参数为蓝图的名字
admin = Blueprint('admin',__name__)

@admin.route('/admin')
def admin_demo():
   return 'admin'



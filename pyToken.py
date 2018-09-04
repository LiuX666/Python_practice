#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者：liux
日期：2018/8/17 13:40
功能：自定义
"""
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
import re

SECRET_KEY = 'hdewrwgejteyeiV'

global dataDict
dataDict={}

def generate_auth_token(name, expiration=18000):
    global dataDict
    s = Serializer(SECRET_KEY, expires_in=expiration)
    g_token=s.dumps({'name': name})
    dataDict[g_token]=name
    return g_token

def verify_auth_token(token):
    s = Serializer(SECRET_KEY)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None  # valid token, but expired
    except BadSignature:
        return None  # invalid token
    return data['name']


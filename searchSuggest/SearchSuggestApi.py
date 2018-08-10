#!/usr/bin/env python
# encoding: utf-8

from flask import Flask,request,make_response
from flask_cors import *
import suggest as suggest
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

tree = suggest.build("./tishi.txt", is_case_sensitive=False)
f = open('./pinyin.json', 'r',encoding= 'utf-8')
pinyinf = json.load(f)

@app.route('/SuggestHanzi',methods=['GET', 'POST','PUT','DELETE'])
def getHanzi():
    # prefix=request.args.get('prefix').encode('utf-8')
    # prefixU = unicode(prefix, "utf-8")
    prefixU=request.args.get('prefix')
    data=getSuggest(prefixU)
    return data

@app.route('/SuggestPinyin',methods=['GET', 'POST','PUT','DELETE'])
def getPinyin():
    prefix = request.args.get('prefix')
    if prefix in pinyinf:
        temp = pinyinf[prefix]
        data = getSuggest(temp)
        return data
    else:
        return json.dumps([], ensure_ascii=False)



def getSuggest(name):
    result = []
    for key, node in suggest.search(tree, name, limit=6):
        dict = {}
        dict['text'] = key
        dict['weight'] = node.weight
        result.append(dict)
    return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
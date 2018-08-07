#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者：liux
日期：2018/8/6 14:03
功能：随机生成不同的验证码图片
"""


import random
import os
from PIL import ImageDraw,ImageFont,Image,ImageFilter


PATH=os.getcwd()
#Arial.ttf 需要自己找，一般电脑自带C:\Windows\Fonts\Arial.ttf
font_file_path=PATH+'/pyUtils/fontSysFiles/Arial.ttf'

def random_check_code(width=120,height=30,char_length=5):
    code = []
    # 背景颜色，默认为白色
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rndChar():
        """
        生成随机字母
        :return:
        """
        return chr(random.randint(65, 90))

    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))

    # 写文字
    font = ImageFont.truetype(font_file_path, 25)
    # font = ImageFont.load_default().font
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text([i * width / char_length, h], char, font=font, fill=rndColor())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())

    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=rndColor())

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE) #加滤镜，可以增加颜色的不同
    return img, ''.join(code)
# -*- coding: utf-8 -*-
# @Author   : LaiJiahao
# @Time     : 2023/2/16 10:33
# @File     : butils.py
# @Project  : B站笔记导出
# @desc     : 信息格式化工具
import json
import os
import re
"""
对cookies进行格式化
"""
def set_settings():
    str_cookie = input("请输入你的cookies:")
    str_csrf = input("请输入你的csrf:")
    str_path = input("请输入笔记导出路径(例如D:\\\\mynote\\\\):")
    cookies = {}
    settings = {"cookies": cookies,
                "csrf": str_csrf,
                "path":str_path}

    try:
        #对拿到的cookie进行两两拆分
        for i in str_cookie.strip('\n').split(";"):
            item = i.split("=")
            key = item[0]
            values = item[1]
            #设置对应关系
            cookies[key] = values
            #存储
            settings['cookies'] = cookies
            settings_size = os.path.getsize('settings.json')
            with open(r'./settings.json', 'w', encoding='utf8') as f:
                # 文件判空
                if settings_size == 0:
                    f.write(json.dumps(settings))
                    f.close()
                if settings_size != 0:
                    f.truncate()
                    f.write(json.dumps(settings))
                    f.close()
        print("cookies和csrf设置成功")


    except:
        print("cookies有误")




"""
获取视频链接的BV号
"""
def find_bvid(url):
    obj = re.compile("/(BV.*?)/")
    return obj.findall(url)[0]


# -*- coding: utf-8 -*-
# @Author   : LaiJiahao
# @Time     : 2023/2/15 19:25
# @File     : main.py
# @Project  : B站笔记导出
# @desc     :
import json
import re
import time

import requests
from note_info import noteInfo
import os
from time import strftime
from time import gmtime
import urllib3

class Bnote:
    def __init__(self,settings):
        self.content = None
        session = requests.session()
        self.session = session
        self.base_path = settings['path']
        self.select_note = None
        self.all_note = None
        self.cookies = settings['cookies']
        self.csrf = settings['csrf']
        self.headers = {
            "referer": "https://www.bilibili.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41"
        }
        session.headers.update(self.headers)
        session.cookies.update(self.cookies)
    """
    获取所有笔记
    :return 返回所有笔记的一个数组
    """
    def get_info(self):

        list_url = "https://api.bilibili.com/x/note/list"
        list_path_params ={
        'pn': 1,
        'ps': 10,
        'csrf': self.csrf
        }
        self.session.keep_alive = False
        try:
            urllib3.disable_warnings()
            response = self.session.get(list_url, params=list_path_params, verify=False)
        except:
            print("链接失败")
        data = response.json()['data']['list']

        #创建一个list存放封装后的信息
        note_info_list = []

        for i in data:
            title = i['title']
            mtime = i['mtime']
            oid = i['arc']['oid']
            bvid = i['arc']['bvid']
            note_id = i['note_id']
            note_info_list.append(
                noteInfo(title,mtime,oid,bvid,note_id).toString()
            )
        self.all_note = note_info_list
        return note_info_list

    """
    获取笔记数据
    :param bvid 视频的bv号
    """
    def get_note(self,bvid):
        #拿到所有的笔记
        self.get_info()
        #拿到所有的BV号
        bv_list = []
        for item in self.all_note:
            bv_list.append(item['bvid'])
        #根据用户的bvid去获取索引
        index = None
        for item in bv_list:
            if item == bvid:
                index = bv_list.index(item)
        self.select_note = self.all_note[index]

        note_url = "https://api.bilibili.com/x/note/info"

        info_path_params = {
            "oid": self.select_note['oid'],
            # TODO oid_type
            "oid_type": " 0",
            "note_id": self.select_note['note_id'],
            # TODO csrf
            "csrf": self.csrf
        }

        response = self.session.get(note_url,params=info_path_params)
        data = response.json()['data']
        return data

    """
    图片下载
    :param img_path 图片存储路径
    :param image_name 图片名称
    :param image_id 图片的id
    """
    def get_image(self,img_path,image_name,image_id):
        img_url = f"https://api.bilibili.com/x/note/image?image_id={image_id}"
        response = self.session.get(img_url)
        with open(img_path + "/" +image_name,"wb") as f:
            f.write(response.content)

    """
    内容解析
    :param content 获取到的json内容
    :param md_path markdown存储路径
    :param img_path 图片存储路径
    """
    def parse_note(self,content,md_path,img_path):

        fp = open(md_path, 'w+', encoding='utf8')

        # 匹配是否是图片
        is_imageUpload = re.compile(r"imageUpload", re.S)
        # 匹配是否是时间戳
        is_tag = re.compile(r"tag", re.S)
        # 匹配图片id
        is_img_id = re.compile(r"image_id=(.*)")

        # 解析
        for line in content:
            line_text = line['insert']

            if is_imageUpload.findall(str(line_text)):
                # 获取图片，下载并写入
                img_info = line_text['imageUpload']
                img_name = img_info['id'] + '.jpg'
                img_id = is_img_id.findall(img_info['url'])[0]
                # 下载图片
                time.sleep(1)
                self.get_image(img_path,img_name, img_id)
                # 转为![]()
                markdown_img = f"![{img_name}](./img/{img_name})"
                fp.write("\n" + markdown_img + "\n")

            elif is_tag.findall(str(line_text)):
                # 格式化时间戳
                tag = line_text['tag']
                tag_time = strftime("%H:%M:%S", gmtime(int(tag['seconds'])))

                time_stamp = f"[{str(tag_time)}](https://www.bilibili.com/video/{self.select_note['bvid']}/?note=&p={tag['index']}&t={tag['seconds']})"
                fp.write("\n" + time_stamp + "\n")
            else:
                fp.write("\n" + str(line_text).strip("\n") + "\n")


    def converter(self,data):
        #获取笔记
        title = data['title']
        content = json.loads(data['content'])
        #使用./title/去存储每一个新的笔记
        title_folder = self.base_path + title


        base_folder = os.path.exists(title_folder) #./title是否存在
        img_folder = os.path.exists(title_folder + title + "/img") #./title/img 是否存在
        if not base_folder:
            os.makedirs(title_folder)
        if not img_folder:
            os.makedirs(title_folder + "/" + "/img")

        md_path = title_folder + "/" + title + ".md"  # 存入./title/title.md
        img_path = title_folder + "/img"  # 存入./title/img/

        self.parse_note(content=content,md_path=md_path,img_path=img_path)
        self.session.close()
        return title_folder





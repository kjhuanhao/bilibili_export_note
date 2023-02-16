# -*- coding: utf-8 -*-
# @Author   : LaiJiahao
# @Time     : 2023/2/15 19:49
# @File     : note_info.py
# @Project  : 未命名
# @desc     :

class noteInfo:
    def __init__(self,title,mtime,oid,bvid,note_id):
        #标题
        self.title = title
        #创建时间
        self.mtime = mtime
        #标识符
        self.oid = oid
        #BV号
        self.bvid = bvid
        #笔记id
        self.note_id = note_id
    def toString(self):
        return {
            "title": self.title,
            "mtime": self.mtime,
            "oid": self.oid,
            "bvid": self.bvid,
            "note_id": self.note_id
        }

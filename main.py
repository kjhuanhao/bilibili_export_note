# -*- coding: utf-8 -*-
# @Author   : LaiJiahao
# @Time     : 2023/2/16 0:28
# @File     : main.py
# @Project  : B站笔记导出
# @desc     : 主运行程序

from bnote import Bnote
import json
from butils import set_settings,find_bvid
import sys


if __name__ == '__main__':
    #检查cookies文件是否正常加载
    print("""
___.   .__.__  ._____.   .__.__  .__                             
\_ |__ |__|  | |__\_ |__ |__|  | |__|                            
 | __ \|  |  | |  || __ \|  |  | |  |                            
 | \_\ \  |  |_|  || \_\ \  |  |_|  |                            
 |___  /__|____/__||___  /__|____/__|                            
     \/                \/                                        
   _____        .__                        .__                   
  /     \_______|  |__  __ _______    ____ |  |__ _____    ____  
 /  \ /  \_  __ \  |  \|  |  \__  \  /    \|  |  \\\\__  \  /  _ \ 
/    Y    \  | \/   Y  \  |  // __ \|   |  \   Y  \/ __ \(  <_> )
\____|__  /__|  |___|  /____/(____  /___|  /___|  (____  /\____/ 
        \/           \/           \/     \/     \/     \/        
       
    """)
    try:
        with open(r'./settings.json', 'r', encoding='utf8') as f:
            settings = json.loads(f.read())
            f.close()
            var = settings['cookies']
            var1 = settings['csrf']
            var2 = settings['path']
    except:
        print('设置异常')
        set_settings()
        #正常退出
        sys.exit(0)
    try:
        b = Bnote(settings)
        #url = input("请输入对应笔记的视频链接:")
        #从运行命令去获取url

        print(sys.argv[-1])
        data = b.get_note(find_bvid(sys.argv[-1]))
        path = b.converter(data)
        print("转换完成，输出到路径：",path)

    except Exception as e:
        print("出现错误，可能是如下两个原因",e)
        print("1. 该视频没有您的笔记")
        print("2. cookies过期需要重新设置")


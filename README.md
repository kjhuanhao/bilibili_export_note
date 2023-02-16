# bilibili_export_note

## 使用前的准备
- Python运行环境（本项目使用的是python3.8）
	- Python网盘下载地址： https://mrhuanhao.lanzoum.com/ixjKG0ibalfg  密码:ddne
	- Python官网下载地址：https://www.python.org/
- Python必备模块
	- requests
		- pip install requests
	- urllib3
		- pip install urllib3

## 必备设置
在首次运行脚本的时候，会自动为你启动设置
- Cookies
- csrf
- path

### 如何获取Cookies和csrf
1. 在B站首页，打开你的开发者工具（按下F12）
2. 点击网络（NetWorks）

![](https://s1.vika.cn/space/2023/02/16/2598b24db93045c192f539ea2a37db9f)

3. 刷新首页，加载数据包
4. 点击搜索按钮（或者按下Ctrl+F）
![](https://s1.vika.cn/space/2023/02/16/ef77155cd0c44ff7bbdeb37cabdb9c52)

5. 搜索`csrf`，找到`info`为头的数据包
![](https://s1.vika.cn/space/2023/02/16/ba3cbbd066a94586ac74422a455474b0)

6. 双击数据包，右侧会弹出信息，找到`请求URL`可以看到`csrf`字段，复制`csrf=`后的字段即可
![](https://s1.vika.cn/space/2023/02/16/a9e2288651f24d4d97836219a5d08508)


7. 往下滚动找到`cookie`，复制`cookie:`后的数据即可
![](https://s1.vika.cn/space/2023/02/16/b046decccb3746529660938b1042ada3)

### 如何运行脚本进行设置
这里以windows为例：
1. 在脚本存放的路径下，打开cmd（可以在地址栏输入cmd然后回车）
![](https://s1.vika.cn/space/2023/02/16/065877a6cbe9402fb5f0b5b91c9ca5ea)

2. 执行命令(输入命令后回车)
```shell
python ./main.py
```
![](https://s1.vika.cn/space/2023/02/16/26a915f79e784846adf663d30fc38e5a)

3. 此时会弹出如下提示，按照提示，将刚刚复制的信息，对应地粘贴进去，然后依次回车
![](https://s1.vika.cn/space/2023/02/16/5f7e2fac989a4c539f4de24c3e2c3b26)

4. 出现配置成功即可
![](https://s1.vika.cn/space/2023/02/16/8b148541fad14b3cb7fcb3580fb902e5)


## 使用脚本
### 命令
```shell
python ./main.py 视频链接
```

### 示例
你无需关注链接的长度和参数，直接粘贴即可
```shell
python ./main.py https://www.bilibili.com/video/BV13F411A7mD/?spm_id_from=333.999.0.0
```


## 扩展
### 配置Obsidian使用
#### 使用的插件
可以在插件市场找到该插件
- [Shell commands](https://github.com/Taitava/obsidian-shellcommands) 

#### 插件配置
- 存放脚本的路径（可以随意），我将脚本放在了`.obsidian/pyscript/`之下
![](https://s1.vika.cn/space/2023/02/16/31c56c4d750a46e5acec789f6d2f7b9c)

- 创建变量
![](https://s1.vika.cn/space/2023/02/16/9a6eda918c72432099ba539229e67642)

- 我的工作目录
`B:\OneDrive\002-Lai'sworkplace\.obsidian`
![](https://s1.vika.cn/space/2023/02/16/09c98e02d8ab4b62a8df9bfb2cde1564)

- 运行命令

![image-20230216144411987](https://s1.vika.cn/space/2023/02/16/33c24c0d6d7b4108b858ef245f401048)

```shell
cd pyscript/bilibili_export_note/ && python ./main.py {{_link}}
```

> 如果你是第一次使用Shell commands，直接将我的插件包导入到plugins即可



## 关于

- 我的B站：[Mrhuanhao](https://space.bilibili.com/67268239)
- 个人博客：[Laijiahao](https://laijiahao.cn)
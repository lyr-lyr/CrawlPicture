# -*- coding:utf-8 -*-
#爬取一张图片

import requests
import os

url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1517834176673&di=28dc7780e6a52fe760db7a6247fe5501&imgtype=0&src=http%3A%2F%2Fn1.itc.cn%2Fimg8%2Fwb%2Frecom%2F2017%2F02%2F21%2F148764886708786252.JPEG"
root = "D://pics//"
path = root + url.split('/')[-1]
try:
	if not  os.path.exists(root):  
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path,'wb') as f:
			f.write(r.content)
			f.close()
			print("图片保存成功")
	else:
			print("文件已存在")
except:
	print("爬取失败")
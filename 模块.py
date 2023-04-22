#coding:utf-8

# #爬取景区天气预报
# import requests
# import re
# url='http://www.weather.com.cn/weather/101010100.shtml'
# #防止反爬
# heads={
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
# }
# resp=requests.get(url,headers=heads)
# #通过修改编码处理乱码
# resp.encoding='utf-8'

# #正则提取，([\u4e00-\u9fa5]*)中括号里就是要提取的内容
# city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
# weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
# wd=re.findall('<span class="wd">(.*)</span>',resp.text)
# zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text)

# #重新组合
# lst=[]
# for a,b,c,d in zip(city,weather,wd,zs):
#     lst.append([a,b,c,d])
# # print(lst)
# for item in lst:
#     print(item)

# #爬取百度logo
# import requests
# url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
# heads={
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
# }
# resp=requests.get(url,headers=heads)

# #因为是图片，所以获取到之后存入磁盘
# with open('logo.png','wb') as file:
#     file.write(resp.content)


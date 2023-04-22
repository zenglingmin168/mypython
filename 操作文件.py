#coding:utf-8
# file=open('a.txt','w+',encoding='gbk')
# lst=['北京','上海','天津']
# file.writelines(lst)
#移动文件指针
# file.seek(0)
# for item in file:
#     print(item)
# file.close()

# 批量创建文件
# import random
# import os.path
# #创建文件名的函数
# def create_filename():
#     filename_lst=[]
#     lst=['水果','烟酒','粮油','肉蛋','蔬菜']
#     code=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#     for i in range(1,1111):
#         #拼接序号
#         filename=''
#         if i<10:
#             filename+='000'+str(i)
#         elif i<100:
#             filename+='00'+str(i)
#         elif i<1000:
#             filename+='0'+str(i)
#         else:
#             filename+=str(i)
        
#         #拼接类别
#         filename+='_'+random.choice(lst)

#         #拼接识别码
#         s=''
#         for j in range(9):
#             s+=random.choice(code)
#         filename+='_'+s
#         filename_lst.append(filename)
#     return filename_lst
# # print(create_filename())

# #创建文件的函数
# def create_file(filename):
#     with open(filename,'w') as file:
#         pass

# #创建文件存放目录
# path='./data'
# if not os.path.exists(path):
#     os.mkdir(path)
# #获取文件名列表
# lst=create_filename()
# for item in lst:
#     create_file(os.path.join(path,item)+'.txt')

# #批量创建文件夹
# import os
# def mkdirs(path,num):
#     for item in range(1,num+1):
#         os.mkdir(path+'/'+str(item))

# path='./newdir'
# if not os.path.exists(path):
#     os.mkdir(path)

# num=eval(input('请输入要创建的目录数量: '))
# mkdirs(path,num)

# #记录用户登陆日志并查看
# import time
# #操作指令函数
# def show_info():
#     print('请输入提示数字，执行相应操作：0.退出 1. 查看登陆日志')

# #记录登陆日志函数
# def write_loginfo(username):
#     with open('log.txt','a') as file:
#         s='用户名：{0}，登陆时间{1}\n'.format(username,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#         file.write(s)
#         print('用户名：{0}，登陆时间{1}')

# #读取登陆日志函数
# def read_loginfo():
#     with open('log.txt','r') as file:
#         while True:
#             line = file.readline()
#             if line=='':
#                 break
#             else:
#                 print(line)

# #输入用户名和密码
# username=input('请输入用户名：')
# pwd=input('请输入密码：')
# if username=='admin' and pwd=='admin':
#     print('登陆成功')
#     write_loginfo(username)
#     show_info()
#     num = eval(input('请输入操作的数字：'))
#     while True:
#         if num == 1:
#             print('查看登陆日志')
#             read_loginfo()
#             show_info()
#         elif num==0:
#             print('退出成功')
#             break
#         else:
#             print('您输入的操作码有误')
#             show_info()
#         num = eval(input('请输入操作的数字：'))
# else:
#     print('您输入的用户名密码有误')

# #模拟淘宝客服自动回复
# def find_answer(question):
#     with open('reply.txt','r',encoding='utf-8') as file:
#         while True:
#             line=file.readline()
#             if line=='':
#                 break
#             #字符串的分割
#             keyword=line.split('|')[0]
#             reply=line.split('|')[1]
#             if keyword in question:
#                 return reply
#     return False

# question=input('HI,xxx您好，小蜜在此等候主人很久了，有什么烦恼快和小蜜说说吧～')
# while True:
#     if question=='bye':
#         break
#     #开始查找是否可以自动回复
#     reply=find_answer(question)
#     if reply==False:
#         question=input('小蜜不知道您在说什么，您可以问一些关于订单、物流、支付的问题，退出请输入bye')
#     else:
#         print(reply)
#         question=input('小主，您还可以问一些关于订单、物流、支付的问题，退出请输入bye')
# print('小主再见')



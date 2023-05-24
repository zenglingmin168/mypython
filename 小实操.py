#coding: utf-8
# #实操一、计算能量消耗
# walk=int(input('请输入当天行走的步数: '))
# power=walk*28
# print('今天共消耗卡路里: '+ str(power) + '(即 ' + str(power/1000) + ' 千卡)')

# #实操二、预测子女身高
# father_high=float(input('请输入父亲身高: '))
# mother_high=float(input('请输入母亲身高: '))
# son_high=(father_high+mother_high)*0.54
# print('预测子女的身高为 {}cm'.format(son_high))

# #实操三、模拟判断支付宝密码是否合法
# pwd=input('请输入支付宝密码: ')
# #写法01
# # if pwd.isdigit():
# #     print('支付密码合法')
# # else:
# #     print('支付密码不合法')
# #写法02
# print('支付密码合法' if pwd.isdigit() else '支付密码不合法')

# #实操四、模拟判断qq账号密码是否正确
# username=input('请输入登陆QQ号: ')
# pwd=input('请输入登陆QQ密码: ')
# if username=='888888' and pwd=='123456':
#     print('登陆成功')
# else:
#     print('用户名密码不正确')

# #实操五、星座分析
# d ={
#     '白羊座':'白羊性格',
#     '金牛座':'金牛性格',
#     '狮子座':'狮子性格'
# }

# star=input('请输入你的星座: ')
# # print(d[star])
# #用get方法时，即使没有输出结果也不会报错
# print(d.get(star))

# #实操六、输出26个字母对应的ASSCII码值
# x=97
# # for _ in range(1,27):
# #     print(chr(x),'----->',x)
# #     x+=1

# while x<123:
#     #chr函数接收一个整数参数，转换成对应的字符
#     print(chr(x),'---->',x)
#     x+=1

# #实操七、模拟用户登录
# for i in range(1,4):
#     username=input('请输入用户名: ')
#     pwd=input('请输入密码: ')
#     if username=='admin' and pwd=='8888':
#         print('登陆成功')
#         break
#     else:
#         print('用户名或密码不正确')
#         if i<3:
#             print(f'你还有{3-i}次机会')
# else:
#     print('对不起，三次均输入错误，请联系后台管理员')

# #实操八、猜数字游戏
# import random
# radm=random.randint(1,100)
# for i in range(1,11):
#     num=int(input('在我心中有个数，请你猜一猜: '))
#     if num<radm:
#         print('小了')
#     elif num>radm:
#         print('大了')
#     else:
#         print('恭喜你，猜对了')
#         break
# print(f'你一共猜了{i}次')
# if i<3:
#     print('哇喔，你太厉害了')
# elif i<7:
#     print('勉强还凑合')
# else:
#     print('你运气太差了')

# #水仙花数
# import math
# for i in range(100,1000):
#     if math.pow((i%10),3)+math.pow((i//10%10),3)+math.pow((i//100),3)==i:
#         print(i)

#千年虫
year=[82,89,88,86,85,00,99]
print('原列表',year)
#用enumerate() 函数同时遍历迭代器中的元素以及元素的索引
for index,value in enumerate(year):
    if str(value)!='0':
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))
print('修改之后的列表',year)

#排序
year.sort()
print('排序后的列表',year)
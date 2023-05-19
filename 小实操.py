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

d ={
    '白羊座':'白羊性格',
    '金牛座':'金牛性格',
    '狮子座':'狮子性格'
}

star=input('请输入你的星座: ')
# print(d[star])
#用get方法时，即使没有输出结果也不会报错
print(d.get(star))
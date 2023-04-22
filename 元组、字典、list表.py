# lst = [10,20,30,40]
# lst.append(('hello','world'))
# print(len(lst))

# #字典整体赋值，指向的是同一个地址，修改一个另外一个也会跟着改变
# d={'a':10,'b':20,'c':30,'d':40}
# d2=d
# d['b']=100
# print(d['b']+d2['b'])

# #列表插入数据
# lst=[1,3,5,7]
# lst.insert(2,[2,20])
# print(lst)

#反转函数reverse的用法
# lst=[1,3,5,7,9]
# print(lst)
# print(lst.reverse())
# print(lst)

# #元组使用注意事项
# t=(10,)
# print(type(t))

# 千年虫
# 方法一：for循环
# lst=[88,89,90,98,00,99]
# print('原列表',lst)
# for index in range(len(lst)):
#     if str(lst[index])!='0':
#         lst[index]='19'+str(lst[index])
#     else:
#         lst[index]='200'+str(lst[index])
# print(lst)

# 方法二：使用enumerate函数
# lst=[88,89,90,98,00,99]
# for index,value in enumerate(lst):
#     if str(value)!='0':
#         lst[index]='19'+str(value)
#     else:
#         lst[index]='200'+str(value)
# print(lst) 

# #模拟京东购物流程
# #1、模拟入库流程
# lst=[]
# for i in range(5):
#     goods=input('请输入商品编号和商品名称进行商品入库，每次只能输入一件商品：')
#     lst.append(goods)
# print('你输入的商品信息为：')
# for item in lst:
#     print(item)

# #2、模拟添加购物车流程
# cars=[]
# while True:
#     flag=False
#     num=input('请输入要购买的商品编号：')
#     for item in lst:
#         if num==str(item[0:4]):
#             flag=True
#             print('你的商品已添加到购物车')
#             cars.append(item)
#             break
#     if not flag and num!='q': # not flag' 是flag=False的简写
#         print('您选择的商品不存在')
#     if num=='q':
#         break

# print('------------------------------')
# print('您购物车已选择的商品为：')
# cars.reverse()
# for item in cars:
#     print(item)
    
#模拟12306车票购票流程
# dict_ticket={
#     'G1509':['北京南-天津南','18:06','18:39','00:33'],
#     'G1510':['北京南-天津南','18:15','18:49','00:34'],
#     'G1511':['北京南-天津西','18:20','11:39','00:59'],
#     'G1512':['北京南-天津南','18:35','19:09','00:34']
# }
# print('车次  出发站-到达站        出发时间     到达时间     历时时长')
# for key in dict_ticket.keys():
#     print(key,end=' ')
#     for item in dict_ticket.get(key):
#         print(item,end='        ')
#     print()

# train_no=input('请输入车次信息：')
# info=dict_ticket.get(train_no,'车次不存在')
# if info!='车次不存在':
#     person=input('请输入乘车人，如果是多位乘客请用逗号隔开：')
#     s=info[0]+' '+info[1]+'开'
#     print('您已购买'+train_no+' '+s+'车票,请'+person+'尽快换取纸质车票【铁路客服】。')
# else:
#     print(info)

#模拟手机通讯录
phones=set({})
for i in range(5):
    info=input('请输入第'+str(i+1)+'朋友的手机号、姓名：')
    phones.add(info)

for j in phones:
    print(j)
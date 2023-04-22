#coding: utf-8

# #车牌归属地
# lst = ['京A88888','津B66666','吉A77766']
# for item in lst:
#     area = item[0:1]
#     print(item,'归属地',area)

#统计字符串在指定字符串中出现的次数
# s='HelloPython,HelloJava,Hellophp'
# word=input('请输入要统计的字符：')
# print('{0}在{1}中一共出现了{2}次'.format(word,s,s.upper().count(word)))
'''
# 这段代码使用了 Python 中字符串的 format() 方法，将统计结果格式化为一个字符串，并将其输出到控制台。
# 具体来说，代码的含义如下：
# 首先使用花括号 {} 来指定要在字符串中插入的占位符。在这个例子中，有三个占位符：{0}、{1} 和 {2}，分别对应第一个参数、第二个参数和第三个参数。
# 然后使用字符串的 format() 方法来进行格式化。在这个例子中，format() 方法接受三个参数，分别是要插入占位符的值。
# 在这个例子中，第一个占位符 {0} 对应的值是 word，即用户输入的要统计的字符或字符串。
# 第二个占位符 {1} 对应的值是 s，即包含要搜索的字符串的字符串。
# 第三个占位符 {2} 对应的值是 s.upper().count(word)，即将 s 中所有字母变成大写字母后，统计 word 在其中出现的次数。
# 最后，使用 print() 函数将格式化后的字符串输出到控制台。
# 需要注意的是，在这个例子中使用了 format() 方法将三个字符串拼接成了一个新的字符串，并将其输出到控制台。这种方式比使用加号 + 进行字符串拼接更加简洁、直观。
同时，使用占位符可以避免出现类型错误，因为 format() 方法会自动将数据转换为字符串类型。
'''

# #格式化输出商品的名称和单价
# lst=[
#     ['01','电风扇','美的',500],
#     ['02','洗衣机','TCL',1000],
#     ['03','微波炉','老板',400]
# ]

# print('编号\t名称\t品牌\t价格')
# for item in lst:
#     for i in item:
#         print(i,end='\t')
#     print()

# #格式化
# print('编号\t名称\t品牌\t价格')
# for item in lst:
#     item[0]='0000'+item[0]
#     item[3]='¥{:.2f}'.format(item[3])
#     for i in item:
#         print(i,end='\t')
#     print()

# #正则表达式提取有效数据
# import re
# s='"quehfdk":"%c3%cd%cdc","hfdka":"美女","khfken":1725,"kjhfkahk":7586892,"gsm":"3c","hfkahdkce":"约100000","hfkhakhfdk":"","hfkdahkjfdhk":0,"hfkahskdhf":1,"data":[{"fdakdjh":"0","fakek":"0","hfkaURL":"https://imq1.baidu.com/it/u=56476467,587462837648&fm=76&fmt=auto","hfkahk":null,"hkfhskhfkd":0,"fhakdURL":"https://imq1.baidu.com/it/u=3543543,596857648&fm=76&fmt=auto","hsfdhiaw":"fhakhsdk","kaekhkc":"","ckahkejcn":0,"hfkdhkURL":"https://imq1.baidu.com/it/u=478798,2634848&fm=76&fmt=auto"}]'
# # 'https://imq1.baidu.com/it/u=56476467,587462837648&fm=76&fmt=auto'
# pattern='https://imq\d{1}.baidu.com/it/u=\d*,\d*&fm=\d*&fmt=auto'
# lst=re.findall(pattern,s)
# for item in lst:
#     print(item)

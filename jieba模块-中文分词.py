#coding: utf-8
import jieba

with open('/Users/mac/mystudy/mypython/华为笔记本.txt','r',encoding='utf-8') as file:
    s=file.read()
# print(s)

#分词
lst=jieba.lcut(s)
# print(lst)

#转换成集合，目的是为了去重
set1=set(lst)
# print(set1)

#使用字典存储词频，key：词，value：出现的次数
d={}
for item in set1:
    if len(item)>=2:
        d[item]=0
# print(d)

#遍历列表，统计词频
for item in lst:
    if item in d:
        d[item]=d[item]+1
# print(d)

#字典再转列表，因为字典不能排序
new_lst=[]
for item in d:
     new_lst.append([item,d[item]])
# print(new_lst)

#按照大列表中的小列表的索引为1的索引排序
new_lst.sort(key=lambda x:x[1],reverse=True)
#只显示前十名
print(new_lst[:10])


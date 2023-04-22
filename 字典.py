# coding:utf-8
d={1001:'李梅',1002:'王华',1003:'张峰'}
print(d)

#字典中添加元素
d[1004]='张三'
print(d)

#获取字典中所有的key
keys=d.keys()
print(keys)

#获取字典中所有的value
values=d.values()
print(values)

#将获取到的结果以更美观的形式展示，比如列表或元组
print(list(values))
print(tuple(values))

#字典遍历
items=d.items()
print(items)
print(list(items))
print(tuple(items))

#元组或列表转换成字典
lst=list(items)
print(lst)
print(dict(lst))

tup=tuple(items)
print(tup)
print(dict(tup))

#指定删除，制定默认值的情况下，如果删除的元素不存在也不会报错；是一个先获取再删除的过程
print(d)
print(d.pop(1005,'不存在'))
# print(d.pop(1005))
print(d)

#随机删除，是一个先获取再删除的过程
print(d.popitem())
print(d)

#删除所有
print(d.clear())
print(d)

#python中一切皆对象，而每一个对象都有一个布尔值，只有少数几个对象的不布尔值为False
print(bool(d))
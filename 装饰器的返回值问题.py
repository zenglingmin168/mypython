#coding: utf-8
'''
通用装饰器是写法
#wrapper：装饰器；fn：目标函数
def wrapper(fn):
    def inner(*args,**kwargs):
        #在目标函数之前执行
        ret = fn(*args,**kwargs)    #执行目标函数
        #在目标函数之后执行
        return ret
    return inner    #千万别加()

@wrapper
def target():
    pass

target()
'''

'''
一个函数可以被多个装饰器装饰
@wrapper1
@wrapper2
def target():
    print('我是目标')
规则和规律：wrapper1 wrapper2 target wrapper2 wrapper1
'''
def wrapper1(fn):
    def inner(*args,**kwargs):
        print('wrapper1进去')
        ret = fn()
        print('wrapper1出来')
        return ret
    return inner

def wrapper2(fn):
    def inner(*args,**kwargs):
        print('wrapper2进去')
        ret = fn()
        print('wrapper2出来')
        return ret
    return inner

@wrapper1
@wrapper2
def target():
    print('我是目标')

target()
#coding: utf-8
'''
1. 函数可以作为参数进行传递
2. 函数可以作为返回值进行返回
3. 函数名称可以当成变量一样进行赋值操作
'''
'''
#装饰器本质上是一个闭包。作用：在不改变原有函数调用的情况下，给函数增加新的功能
def wrapper(fn):    #wrapper:装饰器，fn:目标函数
    def inner(*args,**kwargs):
        #在目标函数执行之前.....
        fn(*args,**kwargs)    #执行目标函数
        #在目标函数执行之后.....
    return inner    #千万别加()
'''
#定义一个装饰器函数
def guanjia(game):
    #inner添加了参数，args一定是一个元祖，用于接收所有的位置参数；kwargs一定是一个字典，用于接收所有的关键字参数
    def inner(*args,**kwargs):
        print('开外挂')
        #*args和**kwargs分别表示把args元祖和kwargs字典打散成位置参数和关键字参数传递进去
        game(*args,**kwargs)
        print('关外挂')
    return inner

#装饰器
@guanjia
def play_dnf(username,password):
    print('我要开始玩dnf了.',username,password)
    print('你好呀，我叫赛利亚，今天又是美好的一天!')

#装饰器
@guanjia
def play_lol(username,password,hero):
    print('我要开始玩lol了.',username,password,hero)
    print('德玛西亚!!!!!')

# play_dnf = guanjia(play_dnf)
# play_lol = guanjia(play_lol)

play_dnf('admin','111111')
play_lol('admin','222222','大盖伦')
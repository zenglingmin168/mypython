#coding: utf-8
'''
1. 函数可以作为参数进行传递
2. 函数可以作为返回值进行返回
3. 函数名称可以当成变量一样进行赋值操作
'''
# def func():
#     print('我是函数')

# def gggg(fn):
#     fn()

# gggg(func)

# def fun1():
#     print('我是函数1')

# def fun2():
#     print('我是函数2')

# fun1=fun2
# fun1()

def guanjia(game):
    def inner():
        print('开外挂')
        game()
        print('关外挂')
    return inner

#装饰器
@guanjia
def play_dnf():
    print('你好呀，我叫赛利亚，今天又是美好的一天!')

#装饰器
@guanjia
def play_lol():
    print('德玛西亚!!!!!')

# play_dnf = guanjia(play_dnf)
# play_lol = guanjia(play_lol)

play_dnf()
play_dnf()
play_lol()
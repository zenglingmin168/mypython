#coding: utf-8
#定义一个父类
class Instrument():
    def make_sound(self):
        pass

#定义一个子类
class Erhu(Instrument):
    def make_sound(self):
        print('二胡在弹奏')

#定义一个子类
class Pinao(Instrument):
    def make_sound(self):
        print('钢琴在演奏')

class Violin(): #默认继承object
    def make_sound(self):
        print('小提琴在演奏')

#编写一个演奏的函数
def play(obj):
    obj.make_sound()    #对象名，打点调用方法

if __name__ == '__main__':
    erhu=Erhu()
    pinao=Pinao()
    violin=Violin()
    play(erhu)
    play(pinao)
    play(violin)

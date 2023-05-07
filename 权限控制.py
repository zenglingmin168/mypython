# coding: utf-8
class Student():
    #收尾双下划线，表示特殊的方法，系统定义
    def __init__(self,name,age,gender):
        #以单下划线开头，表示受保护的属性，只能类本身及子类使用
        self._name=name
        #以双下划线开头，表示私有的，只能类本身使用
        self.__age=age
        #普通实例属性，在类的外部、内部、子类都可以使用
        self.gender=gender

    #以单下划线开头的方法，属于受保护的方法
    def _fun1(self):
        print('受保护的方法，类本身和子类都可以使用')
    #以双下划线开头的方法，属于私有方法
    def __fun2(self):
        print('私有方法，只能类本身使用')
    #普通实例方法，在类的外部使用对象名打点使用
    #在类的内部，使用self打点使用
    def show(self):
        self._fun1()    #类本身使用受保护的方法
        self.__fun2()   #类本身使用私有方法
        print(self._name)   #类本身使用受保护的属性
        print(self.__age)   #类本身使用私有属性
        print(self.gender)  #类本身使用普通属性

if __name__ == '__main__':
    #创建一个Student类型的对象
    stu=Student('张三',25,'女')  
    #使用受保护的实例属性
    print(stu._name)
    #使用私有实例属性
    # print(stu.__age)  #程序报错，在使用类的私有属性时，出了类的定义范围 
    #使用受保护的方法
    stu._fun1()
    #使用私有方法
    # stu.__fun2()    #程序报错，在使用类的私有方法是，出了类的定义范围

    #可以使用如下的方法使用类的私有成员，但是一般不建议这样使用
    #使用类的私有属性
    print(stu._Student__age)
    #使用类的私有方法
    stu._Student__fun2()
    
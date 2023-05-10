#coding: utf-8
class A():
    pass
class B():
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

if __name__ == '__main__':
    a=A()   #创建A类的对象
    b=B()   #创建B类的对象
    c=C('zhangsan',18)  #创建C类的对象
    #对象的属性字典
    print(a.__dict__)
    print(c.__dict__)
    #对象所属的类
    print(a.__class__)
    print(b.__class__)
    print(c.__class__)
    #类的父类，结果是一个元组
    print(A.__bases__)
    print(C.__bases__)
    #类的父类，如果继承了多个父类，结果是第一个
    print(A.__base__)
    print(C.__base__)
    #类的层次结构
    print(A.__mro__)    #A类继承了object类
    print(C.__mro__)    #C类继承了A类和B类，A和B又继承了object类
    #类的子类，结果是列表形式
    print(A.__subclasses__())   #A的子类是C
    print(C.__subclasses__())   #C没有子类，故为空
#coding:utf-8
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'大家好，我是:{self.name}，我今年:{self.age}岁了')

#Student继承Person类
class Student(Person):
    #编写初始化方法
    def __init__(self, name, age, stuno):
        #调用父类的初始化方法，继承方式一
        super().__init__(name, age) #给name和age进行赋值
        self.stuno=stuno    #给自己特有的属性进行赋值

#Doctor类继承Person类
class Doctor(Person):
    def __init__(self, name, age, department):
        #调用父类的初始化方法，继承方式二
        Person.__init__(self, name, age)    #给name和age进行赋值
        self.department=department  #给自己特有的属性进行赋值

if __name__=='__main__':
    #创建Student类的对象
    stu=Student('张三',25,'mn0001')
    stu.show()

    #创建Doctor类的对象
    doc=Doctor('李四',26,'眼科')
    doc.show()



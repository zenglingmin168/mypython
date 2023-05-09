#coding:utf-8
#当父类中的方法不能完全满足子类的需求时，我们可能就需要进行方法重写，通常子类中重写方法时名字会和父类保持一致
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

    #重写父类的方法
    def show(self):
        #可以去调用父类的show方法，也可以重写编写实现方法的代码，显示输出内容
        super().show()
        print(f'我来自xx，我的学号是{self.stuno}')

#Doctor类继承Person类
class Doctor(Person):
    def __init__(self, name, age, department):
        #调用父类的初始化方法，继承方式二
        Person.__init__(self, name, age)    #给name和age进行赋值
        self.department=department  #给自己特有的属性进行赋值

    def show(self):
        print(f'我叫{self.name}，我今年{self.age}，我的岗位是{self.department}')

if __name__=='__main__':
    #创建Student类的对象
    stu=Student('张三',25,'mn0001')
    stu.show()

    #创建Doctor类的对象
    doc=Doctor('李四',26,'眼科')
    doc.show()
class Student:
    #类的属性：类中，方法外的变量
    school='某某教育'

    #初始方法__init__
    def __init__(self,xm,age):  #xm,age 是方法的参数，局部变量
        #=左边是实例属性，=右边是局部变量
        self.name=xm    #将局部变量的值赋值给实例属性self.name
        self.age=age    #实例属性的名字和局部变量的名字相同了
    
    #实例方法：定义在类中，含有默认参数self的函数
    def show(self):
        print(f'我叫:{self.name},今年:{self.age}岁了')

    #类方法
    @classmethod
    def cm(cls):
        print('这里是一个类方法，是不能调用实例子属性和实例方法的')

    #静态方法
    @staticmethod
    def sm():
        print('这里是一个静态方法，是不能调用实例属性和实例方法的')       

#类的组成部分的使用
#创建对象，在创建对象时，会自动调用__init__方法
stu=Student('ysj',18)   #只能传两个，因为__init__方法中自定义的变量只有2个
#使用实例属性：对象名打点使用
print(stu.name,stu.age)
#使用类属性：类名打点使用
print(Student.school)
#使用实例方法：实例名打点调用实例方法
stu.show()
#使用类方法：类名打点调用类方法
Student.cm()
#使用静态方法：类名打点调用静态方法
Student.sm()
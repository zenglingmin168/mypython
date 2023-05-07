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

#创建两个student类型的对象
stu=Student('ysj',18)
stu2=Student('陈梅梅',20)
print(stu.name,stu.age)
print(stu2.name,stu2.age)
#为stu2动态绑定实例属性
stu2.gender='男'
print(stu2.name,stu2.age,stu2.gender)

#定义一个普通函数(方法)
def introduce():
    print('我是一个普通函数，我被动态绑定成了stu2对象的方法')

#为实例stu2动态绑定该方法
stu2.fun=introduce
stu2.fun()
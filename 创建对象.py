class Student:
    #类的属性：类中，方法外的变量
    school='某某教育'

    #实例属性。其中__init__是初始方法
    def __init__(self,xm,age):  #xm,age 是方法的参数，局部变量
        #=左边是实例属性，=右边是局部变量
        self.name=xm    #将局部变量的值赋值给实例属性self.name
        self.age=age    #实例属性的名字和局部变量的名字相同了
    
    #实例方法：定义在类中，含有默认参数self的函数
    def show(self):
        print(f'我叫:{self.name},今年:{self.age}岁了')
Student.school='xxx教育'
#创建N多个对象
stu=Student('ysj',18)
stu2=Student('陈梅梅',20)
stu3=Student('马丽',23)
stu4=Student('marry',24)
# print(type(stu))
# print(type(stu2))
# print(type(stu3))
# print(type(stu4))
Student.school='xxx教育'
# print(stu.name,stu.age)

lst=[stu,stu2,stu3,stu4]
for item in lst:
    item.show()
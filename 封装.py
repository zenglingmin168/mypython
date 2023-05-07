#coding: utf-8
# class Student():
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age

#     def show(self):
#         print(f'我叫{self.__name}, 我今年{self.__age}')

# if __name__ == '__main__':
#     #程序运行没有报错，但是运行结果不符合实际情况，因为年龄被赋予了不正确的值，所以程序不够健壮
#     stu=Student('张三',-26)
#     stu.show()

class Student():
    def __init__(self,name):
        self.__name=name
    #使用@property装饰器
    @property
    def age(self):
        return self.__age
    
    #设置赋值操作
    @age.setter
    def age(self,value):
        if value<0 or value>130:
            print('年龄不在正确的区间范围，设置年龄的范围应该是0-130之间')
            self.__age=18
        else:
            self.__age=value

    def show(self):
        print(f'{self.__name}, 我今年{self.__age}')

if __name__ == '__main__':
    #创建Student类型的对象
    stu=Student('张三')
    stu.age=-23
    # print(stu.age)
    stu.show()
    # stu.age=20
    # stu.show()
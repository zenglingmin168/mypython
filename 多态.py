#coding:utf-8
class Person():
    def eat(self):
        print('人，喜欢吃五谷杂粮')

class Cat():
    def eat(self):
        print('猫，喜欢吃鱼')

class Dog():
    def eat(self):
        print('狗，喜欢啃骨头')

def fun(obj):   #函数的定义处，obj是函数的形式参数
    obj.eat()   #对象名打点调用eat方法

if __name__ == '__main__':
    person=Person() #创建Person类型的对象person
    cat=Cat()       #创建Cat类型的对象cat
    dog=Dog()       #创建Dog类型的对象dog

    #调用fun函数
    fun(person) #python中的多态不关心对象的数据类型，只关心对象中是否有同名的方法
    fun(cat)
    fun(dog)
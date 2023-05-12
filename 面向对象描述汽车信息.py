class Cars():
    #父类初始化属性
    def __init__(self,type,no):
        self.type=type
        self.no=no

    #父类方法
    def start(self):
        print('我是车，我能启动')

    #父类方法
    def stop(self):
        print('我是车，我能停止')

#子类Taxi
class Taxi(Cars):
    def __init__(self, type, no, company):
        #继承父类的属性
        super().__init__(type, no)
        #子类自己的属性
        self.company=company

    #start方法重写
    def start(self):
        print('乘客您好！')
        print(f'我是{self.company}出租车公司的，我的车牌是{self.no},您要去哪里？')

    #stop方法重写
    def stop(self):
        print('目的地到了，请您付款下车，欢迎下次乘坐')

#子类Familycar
class Familycar(Cars):
    def __init__(self, type, no, name):
        #继承父类的属性
        super().__init__(type, no)
        #子类自己的属性
        self.name=name

    #方法重写
    def start(self):
        print(f'我是{self.name}, 我的汽车我做主')

    #方法重写
    def stop(self):
        print('目的地到了，我们去玩吧')

if __name__ == '__main__':
    #创建出租车类的对象
    taxi=Taxi('丰田','粤B65766','滴滴')
    taxi.start()
    taxi.stop()
    #创建家用汽车类的对象
    famicar=Familycar('宝马','湘A67587','章三')
    famicar.start()
    famicar.stop()

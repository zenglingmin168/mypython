class Circle:
    def __init__(self,r):
        self.r=r

    #计算圆的面积的方法
    def get_area(self):
        return 3.14*self.r**2
    
    #计算圆的周长的方法
    def get_perimeter(self):
        return 3.14*2*self.r
    
if __name__ == '__main__':
    r=eval(input('请输入圆的半径: '))
    #创建Circle类的对象
    cir=Circle(r)
    #调用计算圆面积的方法计算圆面积
    area=cir.get_area()
    #调用计算圆周长的方法计算圆周长
    perimeter=cir.get_perimeter()
    print('圆的面积为：',area)
    print('圆的周长为：',perimeter)
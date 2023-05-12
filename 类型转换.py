#coding: utf-8
def fun():
    num=int(input('请输入一个十进制的整数: '))    #将str类型转换成int类型
    print(num,'的二进制数为: ',bin(num))    #第一种写法，使用位置可变的位置参数
    print(str(num)+' 的二进制数为: '+bin(num))  #第二种写法，使用“+”作为连接符（+的作用均为str类型）
    print('%s 的二进制数为: %s' % (num,bin(num)))   #第三种写法，使用“%”格式化字符串
    print('{0} 的二进制数为: {1}'.format(num,bin(num))) #第四种写法，使用format函数格式化字符串
    print(f'{num} 的二进制数为: {bin(num)}')    #第五种写法，使用“f”格式化字符串
    print('---------------------------------------')
    print(f'{num} 的八进制数为: {oct(num)}')
    print(f'{num} 的十六进制数为: {hex(num)}')

if __name__ == '__main__':
    while True:
        #异常处理
        try:
            fun()
            break
        except:
            print('只能输入整数！程序出错，请重新输入')

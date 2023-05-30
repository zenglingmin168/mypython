#coding: utf-8
def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function

closure=outer_function(10)
result=closure(5)
print(result)
'''
闭包在Python中具有广泛的应用，可以用于创建高阶函数、实现装饰器、延迟计算和缓存等场景。
在上述示例中，outer_function 是外部函数，它接受一个参数 x。
在外部函数中，我们定义了一个内部函数 inner_function，它接受参数 y，并返回 x + y 的结果。
然后，外部函数返回内部函数 inner_function。
通过调用外部函数，并将返回的内部函数赋值给变量 closure，我们创建了一个闭包。
最后，我们可以通过调用闭包 closure 来访问和使用外部函数的变量，得到结果 15。
'''
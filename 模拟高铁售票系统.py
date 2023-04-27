#coding: utf-8
import prettytable as pt

#显示坐席函数
def show_ticket(row_numer):
    #创建表格
    tb=pt.PrettyTable()
    #设置表格字段
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    #遍历初始化有票
    for i in range(1,row_numer+1):
        lst=[f'第{i}行','有票','有票','有票','有票','有票']
        #往表格中添加数据
        tb.add_row(lst)
    print(tb)

def order_ticket(row_number,row,column):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(1,row_number+1):
        #当遍历到的行和选择的行一样时，就修改该行所选的列的值
        if int(row)==i:
            lst=[f'第{i}行','有票','有票','有票','有票','有票']
            #根据索引来修改对应的值
            lst[int(column)]='已售'
            tb.add_row(lst)
        else:
            lst=[f'第{i}行','有票','有票','有票','有票','有票']
            tb.add_row(lst)
    print(tb)


if __name__ == '__main__':
    row_numer=6
    #显示所有坐席
    show_ticket(row_numer)
    #显示订票后的坐席
    choose_num=input('请输入选择的坐席，比如4,3表示第4行第3列：')
    row,column=choose_num.split(',')
    order_ticket(row_numer,row,column)

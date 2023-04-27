#coding: utf-8
import openpyxl

#先读取工作簿
wb=openpyxl.load_workbook('/Users/mac/mystudy/mypython/景区天气数据.xlsx')
#再读取表
sheet=wb['景区天气']
#表格数据是一个二维数据，先读取行再读取列
lst=[]
#再读取行
for row in sheet.rows:
    sublst=[]
    #再读取列
    for cell in row:
        sublst.append(cell.value)
    lst.append(sublst)
for item in lst:
    print(item)

input()
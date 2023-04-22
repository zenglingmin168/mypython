#coding: utf-8
import weather
import openpyxl
lst=weather.parse_html(weather.get_html())
# print(lst)

#创建工作簿
workbook=openpyxl.Workbook()
#创建表
sheet=workbook.create_sheet('景区天气')
#将数据写入表
for item in lst:
    sheet.append(item)
workbook.save('景区天气数据.xlsl')
#coding: utf-8
import pdfplumber

#打开pdf文件
with pdfplumber.open('/Users/mac/Downloads/ELK总结03-01的副本.pdf') as pdf:
    for i in pdf.pages:
        print('------------------------')
        #提取每一页的文本内容
        print(i.extract_text())


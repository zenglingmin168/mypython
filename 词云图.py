#coding: utf-8
import jieba
from wordcloud import WordCloud 

#打开并读取文件的所有行
with open('/Users/mac/mystudy/mypython/华为笔记本.txt','r',encoding='utf-8') as file:
    s=file.read()

#分词
lst=jieba.lcut(s)
# print(lst)

#排除词
stopword=['操作系统','ThinkPad','Windows','笔记本','这些','使用Windows操作系统','少量接口需要使用转接头','这些品牌的笔记本具有各自的特点和优势','优点','缺点']
#合并成文本
txt=''.join(lst)
# print(txt)

#设置词云图限制条件
wordcloud=WordCloud(background_color='white',font_path='/Users/mac/Downloads/simhei/SimHei.ttf',stopwords=stopword,width=800,height=600)
#有txt文本生成词云图
wordcloud.generate(txt)
#将词云图保存成图片
wordcloud.to_file('词云图.png')
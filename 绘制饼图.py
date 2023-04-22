import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 创建 FontProperties 对象
font_prop = fm.FontProperties(fname='/Users/mac/Downloads/simhei/SimHei.ttf')

#读取excel表
df=pd.read_excel('京东手机销售数据.xlsx')
# print(df)
#解决中文乱码问题
# plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['font.sans-serif'] = ['/Users/mac/Downloads/simhei/SimHei.ttf']
#解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False
#设置画布大小
plt.figure(figsize=(10,6))
#获取商品名称
labels=df['商品名称']
#获取商品销量
y=df['北京出库销量']
# print(labels,y)
#绘制饼图，并保留1位浮点数
plt.pie(y,labels=labels,autopct='%1.1f%%',textprops={'fontproperties': font_prop})
#设置x,y轴刻度一致，保证饼图是一个圆形
plt.axis('equal')
plt.title('手机销量',fontproperties=font_prop)
#显示图形
plt.show()

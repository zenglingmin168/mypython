from PIL import Image
#加载图片
im = Image.open('/Users/mac/mystudy/mypython/hua.jpg')
#提取RGB图像的颜色通道，返回的是图像的副本
r, g, b = im.convert('RGB').split()  # 将图像转换为RGB模式后拆分
# print(r)

#合并通道，其中mode表示色彩，bands表示新的色彩通道
om=Image.merge(mode='RGB',bands=(r,b,g))
om.save('/Users/mac/mystudy/mypython/new-hua.jpg')
# om.show()

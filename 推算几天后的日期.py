import datetime

def input_date():
    inputdate=input('请输入开始日期（如20230120）后按回车：')
    #截取字符串并格式拼接成某种格式，方便后面转换格式
    datestr=inputdate[0:4]+'-'+inputdate[4:6]+'-'+inputdate[6:]
    #转换数据类型及格式，方便运算
    dt=datetime.datetime.strptime(datestr,'%Y-%m-%d')
    return dt

if __name__ == '__main__':
    date=input_date()
    print(date,type(date))
    in_day=eval(input('请输入天数：'))
    #运算
    date=date+datetime.timedelta(in_day)
    #用占位符来输出来是输出结果更美观
    print('%d 天后的日期是 %s' % (in_day,date))
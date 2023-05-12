class Student:
    def __init__(self,name,age,gender,num):
        self.name=name
        self.age=age
        self.gender=gender
        self.num=num

    def info(self):
        print(self.name,self.age,self.gender,self.num)

if __name__ == '__main__':
    print('请输入五位学生信息：（姓名#年龄#性别#成绩）')
    lst=[]
    for i in range(1,6):
        s=input(f'请输入第{i}位学生成绩信息：')
        s_lst=s.split('#')
        stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
        lst.append(stu)

    for item in lst:
        item.info()
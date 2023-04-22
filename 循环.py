# coding: utf-8

#简单无限循环
# answer='y'
# while answer=='y':
#     print('好好学习，天天向上')
#     answer=input('今天要上课吗?y/n')

# #累加求和
# #初始化
# s = 0
# i = 1
# #条件判断
# while i<=100:
#     s+=i
#     i+=1
# #print('1到100之间到累加和为：',s)
# #语句块
# else:
#     print('1到100之间到累加和为：',s)

#模拟登陆次数限制
# i = 0
# while i < 3:
#     user_name=input('请输入用户名：')
#     passwd=input('请输入密码：')
#     if user_name=='admin' and passwd=='123456':
#         print('系统正在登陆')
#         #登陆成功时通过改变循环条件让它退出循环
#         i = 6
#     else:
#         print('你还有',2 - i,'次机会')
#         #输入失败时通过改变i的值以使输入机会递减
#         i+=1
# if i == 3:
#     print('你3次均输入错误，请5分钟后再试')

#输出简单图形(外循环控制行输出，内循环控制列输出)
#长方形或正方形
# for i in range(1,4):
#     for j in range(1,5):
#         print('*',end='')
#     print()

#正三角
# for i in range(1,6):
#     for j in range(1,i+1):
#         #不换行
#         print('*',end='')
#     #换行
#     print()

#倒三角
# for i in range(1,6):
#     for j in range(1,7-i):
#         print('*',end='')
#     print()

#等边三角形（其实是有一个到三角形和一个等边三角形组成的）
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(' ',end='')
#     for k in range(1,i*2):
#         print('*',end='')
#     print()

#输出菱形
# row = eval(input('请输入菱形的行数：'))
# while row%2 == 0:
#     row = eval(input('请输入菱形的行数：'))
# top_row = (row+1)//2
# for i in range(1,top_row+1):
#     for j in range(1,top_row+1-i):
#         print(' ',end='')
#     for k in range(1,i*2):
#         print('*',end='')
#     print()
# bottom_row = row//2
# for i in range(1,bottom_row+1):
#     for k in range(1,i+1):
#         print(' ',end='')
#     for j in range(1,2*(bottom_row+1)-2*i):
#         print('*',end='')
#     print()

#输出空心菱形
# row = eval(input('请输入菱形的行数：'))
# while row%2 == 0:
#     row = eval(input('请输入菱形的行数：'))
# top_row = (row+1)//2
# for i in range(1,top_row+1):
#     for j in range(1,top_row+1-i):
#         print(' ',end='')
#     for k in range(1,i*2):
#         if k ==1 or k == (2*i -1):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()
# bottom_row = row//2
# for i in range(1,bottom_row+1):
#     for k in range(1,i+1):
#         print(' ',end='')
#     for j in range(1,2*(bottom_row+1)-2*i):
#         if j == 1 or j == (2*(bottom_row+1)-2*i -1):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

# #chatgpt给的空心菱形代码
# size = 5
# # 输出上半部分
# for i in range(size):
#     for j in range(size-i-1):
#         print(" ", end="")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i or i == size-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# # 输出下半部分
# for i in range(size-2, -1, -1):
#     for j in range(size-i-1):
#         print(" ", end="")
#     for j in range(2*i+1):
#         if j == 0 or j == 2*i or i == size-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#判断闰年
# year=eval(input('请输入一个年份：'))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(year,'年是闰年')
# else:
#     print(year,'年是平年')

# #模拟10086按键查询功能
# #(1)初始化变量
# answer='y'
# #(2)条件判断
# while answer=='y':
#     print('-------欢迎来到10086查询功能-------')
#     print('1. 查询当前余额')
#     print('2. 查询当前的剩余流量')
#     print('3. 查询当前的剩余通话时长')
#     print('0. 退出系统')
#     choice=input('请输入你要执行的操作：')
#     if choice=='1':
#         print('当前余额为666.6')
#         print()
#     elif choice=='2':
#         print('当前的剩余流量为8G')
#         print()
#     elif choice=='3':
#         print('当前的剩余通话时长为88.8分钟')
#         print()
#     elif choice=='0':
#         print('程序退出，谢谢您的使用！')
#         break
#     else:
#         print('对不起，输入有误，请重新输入')
#         print()
#     #（3）改变变量
#     answer=input('还继续操作吗y/n')
# else:
#     print('程序退出，谢谢您的使用！')

# #九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(j)+'*'+str(i)+'='+ str(i*j),end='\t')
#     print()

# #猜数字游戏
# import random
# rand=random.randint(1,100)
# count=1
# while count<=10:
#     number=eval(input('在我心中有个数，在1-100之间，请你猜一猜: '))
#     if rand==number:
#         print('恭喜你，猜对了')
#         break
#     elif rand<number:
#         print('不好意思，大了')
#     else :
#         print('不好意思，小了')
#     count+=1

# if count<=3:
#     print('你运气真好')
# elif count<=6:
#     print('还不错')
# else:
#     print('就是猜的次数有点多')

#猜拳游戏
import random

def get_player_choice():
    # 获取玩家输入
    player_choice = input("请出拳（石头/剪刀/布）：")
    # 判断玩家输入是否合法
    while player_choice not in ["石头", "剪刀", "布"]:
        print("输入有误，请重新输入！")
        player_choice = input("请出拳（石头/剪刀/布）：")
    return player_choice

def get_computer_choice():
    # 随机生成电脑出拳
    computer_choice = random.choice(["石头", "剪刀", "布"])
    return computer_choice

def get_result(player_choice, computer_choice):
    # 判断胜负并返回结果
    if player_choice == computer_choice:
        return "平局"
    elif player_choice == "石头" and computer_choice == "剪刀" or \
         player_choice == "剪刀" and computer_choice == "布" or \
         player_choice == "布" and computer_choice == "石头":
        return "玩家胜利"
    else:
        return "电脑胜利"

def main():
    print("欢迎来到猜拳游戏！")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print("玩家出拳：", player_choice)
        print("电脑出拳：", computer_choice)
        result = get_result(player_choice, computer_choice)
        print(result)
        choice = input("是否继续游戏？（是/否）")
        if choice == "否":
            break
    print("游戏结束！")

if __name__ == "__main__":
    main()

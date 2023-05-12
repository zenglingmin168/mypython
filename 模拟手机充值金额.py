#coding: utf-8
print('用户手机账户原有话费金额为: \033[0;35m8元\033[m')
money=int(input('请输入手机充值金额: '))
money+=8
print('当前账户余额为: \033[0;35m',money,'元\033[m')
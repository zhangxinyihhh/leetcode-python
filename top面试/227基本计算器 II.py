# -*- coding:utf-8 -*-
class Solution:
    def calculate(self, s: str) -> int:
        # 1.用字典存储加入符号后的运算结果
        # 2.用匿名函数表达加入符号的运算过程
        # 3.优先级高的符号：栈
        #   乘法：若出现*，本次数字*上一次存储的最后一个数字
        #   除法：若出现/，需注意-3//2=-2,int(-3/2)=-1
        res = []
        sign_dic = {
            '+': lambda x: res.append(x),
            '-': lambda x: res.append(-x),
            '*': lambda x: res.append(x * res.pop()),
            '/': lambda x: res.append(int(res.pop() / x))
        }
        num = 0
        sign = '+'  # 为了将第一个数强行加入res
        for ss in s + '+':
            if ss.isdigit():
                num = num * 10 + int(ss)  # 可能是多位数
            elif ss != ' ':
                sign_dic[sign](num)
                sign = ss
                num = 0
        return sum(res)

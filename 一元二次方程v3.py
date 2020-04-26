#一元二次方程v3.py
import math as ma
import cmath as cma
import random as r

def delta(u,i,o):
    return i*i-4*u*o

def fun(uu,ii,oo):
    if delta(uu,ii,oo) >= 0:
        x1 = ((-ii)+ma.sqrt(delta(uu,ii,oo)))/(4*a)
        x2 = ((-ii)-ma.sqrt(delta(uu,ii,oo)))/(4*a)
        return print("x1 = {:.4} x2 = {:.4}".format(x1,x2))
    else:
        x1 = ((-ii)+cma.sqrt(delta(uu,ii,oo)))/(4*a)
        x2 = ((-ii)-cma.sqrt(delta(uu,ii,oo)))/(4*a)
        return print("x1 = {:.4} x2 = {:.4}".format(x1,x2))

def is_number(s):                        
    try:
        float(s)
        return True
    except ValueError:
        return False

def judgement(xx):                      
    if is_number(xx)==True:     
        return xx
    else:
        while is_number(xx)==False:      
            print("参数错误")
            cc =input("请重新输入:")
            if is_number(cc)==True:
                return cc

ps = input("开始? y/n ")
while ps == 'y':
    mode = input("是否采用随机数填充系数？ y/n ")
    if mode == 'y':
        a = r.uniform(-20,20)
        b = r.uniform(-25,25)
        c = r.uniform(-15,15)
    else:
        print("请输入二次项系数:")
        a = float(judgement(input()))
        print("请输入一次项系数:")
        b = float(judgement(input()))
        print("请输入常数项")
        c = float(judgement(input()))

    print("----------------------------------------")
    print("({:.4})x^2 + ({:.4})x + ({:.4}) = 0 ".format(a,b,c))
    print("----------------------------------------")
    pk = input("请确认系数无误后即可求解！ y/n ")
    fun(a,b,c)
    ps = input("继续/重来？ y/n ")
print("结束")

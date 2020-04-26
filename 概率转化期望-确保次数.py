#概率转化期望/确保次数.py
import math as ma

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def judgment(xx):
    if is_number(xx) == True:
        return xx
    else:
        while is_number(xx) == False:
            print("输入错误！")
            cc = input("请输入数字 ")
            if is_number(cc) == True:
                return cc

def is_in(ss):
    if ss in ['类型一','类型二','一','二','1','2']:
        return True
    else:
        return False

def isin(sss):
    if is_in(sss) == True:
        return sss
    else:
        while is_in(sss) == False:
            print("输入错误")
            ccc = input("请输入 类型一/类型二/一/二/1/2 ")
            if is_in(ccc) == True:
                return ccc


def main():
    K = input("开始？ y/n ")
    while K == 'y':
        print("本工具可计算期望次数和确保次数，请选择您需要的模式")
        ps = input("请输入模式代号: 1表示计算期望次数 2表示计算确保次数")
        if ps == '1':
            print("类型一：在一个池子里做放回抽样（即打boss刷战甲）")
            print("类型二：单独敌人放回抽样（即刷某些敌人掉落）")
            b = isin(input("请选择类型: "))
            if b in ['类型一','一','1']:
                c = int(judgment(input("有几个东西？")))
                app = []
                for i in range(0,c):
                    m = c/(i+1)
                    app.append(m)
                Sum = sum(app)
                e1 = ma.floor(Sum)
                e2 = ma.ceil(Sum)
                print("转化后的期望次数为: {}~{}次".format(e1,e2))
                K = input("继续? y/n ")
            else:
                p = float(judgment(input("请输入掉落概率 ")))
                n = 1/p
                n1 = ma.floor(n)
                n2 = ma.ceil(n)
                print("转化后的概率为: {}~{}次".format(n1,n2))
                K = input("继续? y/n ")
        else:
            p1 = float(judgment(input("请输入获取概率: ")))
            many = float(judgment(input("请输入确保概率(0.99 0.999 0.9999等): ")))
            s1 = ma.log(1-many,10)
            s2 = ma.log(1-p1,10)
            equal1 = ma.floor(s1/s2)
            equal2 = ma.ceil(s1/s2)
            print("转化后的次数为: {} ~ {} 次".format(equal1,equal2))
            K = input("继续? y/n ")

main()

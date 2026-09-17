#26+35
import sys
a=input("输入运算")
yunsuanfu=0
if "+" in a:
    yunsuanfu = "+"
elif "-" in a:
    yunsuanfu = "-"
elif "*" in a:
    yunsuanfu = "*"
elif "/" in a:
    yunsuanfu = "/"
if yunsuanfu == 0:
    print("杂鱼主人连计算式都数不对吗（憋笑）")
    sys.exit()
b = a.find(yunsuanfu)
f = str(a[:b].strip())
l = str(a[b+1:].strip())
if not f or not l:
    print("杂鱼主人连计算式都数不对吗（憋笑）")
    sys.exit()
else:
    f = float(f)
    l = float(l)
if yunsuanfu == "+":
    print(f+l)
elif yunsuanfu == "-":
    print(f-l)
elif yunsuanfu == "*":
    print(f*l)
elif yunsuanfu == "/":
    if l == 0:
        print("笨蛋主人不知道0不能做分母吗？")
    else:
        print(f/l)
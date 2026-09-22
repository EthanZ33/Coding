# zako={
#     "name":"合法萝莉",
#     "age":"18",
#     "school":"西交",
#     "affection":"萝莉"
# }
# print(zako)
# print(zako["affection"])
# print(zako.get("game","无"))
# print(zako.get("name","0"))
# print("name" in zako)
# a = zako.pop("name",'none')
# print(a)
# print("name" in zako)
# print(f"{list(zako.keys())}\n{list(zako.values())}")
# for key in zako.items():
#     print(key)
# for s in zako.values():
#     print(s)
# for a,b in zako.items():
#     print(a,b)
# zako_1=dict(sorted(zako.items()))
# print(zako_1)
# amount = {x : x * x for x in range(1,10) if x % 2 != 0}
# print(list(amount.items()))
# zako_2=zako.copy()
# zako_2["true_name"]="非法萝莉"
# print(zako_2)
# zako_3 = zako | zako_2
# print(zako_3)
#毕业项目：
menu = {"烤鱼": 20, "海带汤": 8, "章鱼小丸子": 15, "汽水": 5}
for dish_unbook,price in menu.items():
    print(f"{dish_unbook}价格是{price}")
print("如果点完了记得输入‘点完了’捏~")
print("如果杂鱼你要删除某一道菜，可以用“删 菜名”哦！")
price = 0
c_menu = {"烤鱼":0,"海带汤":0,"章鱼小丸子":0,"汽水":0}
while True:
    a = input("请输入你要点的菜品：")
    if a in menu:
        price += menu[a]
        c_menu[a] += 1
    elif a.startswith("删") and a[2:] in c_menu.keys() and c_menu[a[2:]]> 0:
        c_menu[a[2:]] -= 1
        print(f"删除成功！\n杂鱼目前点了{c_menu[a[2:]]}份{a[2:]}")
        price -= menu[a[2:]]
    #优化如上，下面是我写的
    # if a == "烤鱼":
    #     price += 20
    # elif a == "海带汤":
    #     price += 8
    # elif a == "章鱼小丸子":
    #     price += 15
    # elif a == "汽水":
    #     price += 5
    elif a == "点完了":
        break
    else:
        if a.startswith("删"):
            if a[2:] in menu:
                print("杂鱼你还没点这道菜呢")
            else:
                print("杂鱼，没有这道菜！")
        else:
            print("杂鱼，没有这道菜！")
zhangdan = []
for dishes,amount in c_menu.items():
    if amount > 0:
        zhangdan.append(((float(menu[dishes]))*float(amount),dishes,amount))
zhangdan.sort(reverse=True)
#错误思路：只用列表写（杂鱼老师乱教！）
# zhangdan = []
# for i,j in menu.items():
#     x = float(c_menu[i])*float(menu[j])
#     zhangdan.append(x)
# zhangdan.sort(reverse=True)
print("您的菜单如下：")
for i,j,k in zhangdan:
    print(f"{j}x{k}----共{i}元")
#下面是不用排序的菜单：
# for dishes,amount in c_menu.items():
#     if amount > 0:
#         print(f"{dishes}*{amount}")
print(f"总价是：{price}")
#pop练习
a=[6,5,4,3,2,1]
c=a.pop(1)
print(a)
print(c)

#len练习
print(len(a))

#remove练习
b=[6,5,4,3,2,1,2,1]
b.remove(1)
print(b)

#sort练习
print(b)
print(sorted(b))
print(b)
b.sort()
print(b)

#count练习/reverse练习
m=[1,3,5,7,9,7,5,3,114514]
print(m.count(7))
m.reverse()
print(m)

#for循环练习
k=['qu','daqu','jiahao','sb','chaoxiong']
x=0
for i  in k:
    print(f"{i.title()}，是个傻逼！")
for j in range(1,11):
    x+=j
print(f"1加到10的和是{x}")

#range函数练习
e=list(range(1,11,2))
print(e)

#如何输出1到10的平方和
square=[]
sums=0
for t in range(1,11):
    square.append(t**2)
    sums=sums+square[t-1]
print(square)
print(sums)
print(f"{sum(square)},{max(square)},{min(square)}")

square2=[l**2 for l in range(1,11)]
print(square2)
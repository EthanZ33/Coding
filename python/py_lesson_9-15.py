#f-string练习
print("小明最爱吃{}".format("苹果"))
value=12.34567
print(f"result:{value:{10}.{3}}")
#endswith方法
a = 'python programing is fun'
a = a.endswith("fun")
print(a)
#字符串练习
first_name="Zhao"
last_name="Ethan"
print(str("{a} {b}").format(a=last_name,b=first_name))
print(f"{last_name} {first_name}")
#换行和空格符号练习
print("Ah, music. A 'magic' beyond all we do here!\nBy Albus Dumbledore")
#和for循环结合
word="chatgpt"
index=1
for i in word:
    print(f"{i}是第{index}个字母")
    index += 1
a = 5
print(f"{a=}")
string_1="goose"
string_2="rose"
for j in string_1:
    if j in string_2:
        print(f"{j}同时在两个单词里出现！")
m=str(input("第一个单词："))
n=str(input("第二个单词："))
d=0
for k in m:
    if k in n:
        print(f"{k}同时在两个单词出现！")
        d=1
if d == 0:
    print("没有共同单词捏")
    
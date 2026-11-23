# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end=" \t")
    print()


# 猜大小游戏
import random
number = random.randint(1, 100)
guess = int(input("请输入您猜的数字:"))
while guess != number:
    if guess < number:
        print("不好意思，您猜小了~")
    else:
        print("不好意思，您猜大了~")
    guess = int(input("请您再猜想一次"))
print("感谢您，您猜对了！")

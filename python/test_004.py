import random


# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)

# 猜数字游戏
# 计算出一个1~100之间的随机数有人来猜
# 计算机根据人猜的数字分别
# 给出提示大一点/小一点/猜对了


computer_number = random.randint(1, 100)
# print(computer_number)

while True:
    user_number = int(input("请输入您要猜的数字："))

    if user_number > computer_number:
        print("大了点")
    elif user_number < computer_number:
        print("小了点")
    elif user_number == computer_number:
        print("猜对啦")
        break


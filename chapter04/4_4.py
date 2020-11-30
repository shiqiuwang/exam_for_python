import random

random.seed = 2020
target = random.randint(1, 100)

while True:
    guess = eval(input("请输入你的猜测:"))
    if type(guess) != int:
        guess = eval(input("输入内容必须为整数:"))
    if guess > target:
        print("猜大了，请重新猜测！")
    elif guess < target:
        print("猜小了，请重新猜测！")
    else:
        print("恭喜，猜对了！")
        break

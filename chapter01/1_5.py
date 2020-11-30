import random

str1 = input("请输入你的名字：")
print("Hello!{}".format(str1))
guard = ord(str1[0]) % 100
print("你的幸运数字是：", random.choice(range(guard)))

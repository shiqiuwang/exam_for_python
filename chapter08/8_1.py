year = eval(input("请输入一个年份："))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("输入的年份是闰年")
else:
    print("输入的年份不是闰年")

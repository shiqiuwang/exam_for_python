num1 = eval(input("请输入第一个整数："))
num2 = eval(input("请输入第二个整数："))

if num1 > num2:
    smaller = num2
else:
    smaller = num1

for i in range(1, smaller + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        gcd = i

lcm = int(num1 * num2 / gcd)

print("{}和{}的最大公约数是：{}".format(num1, num2, gcd))
print("{}和{}的最小公倍数是：{}".format(num1, num2, lcm))

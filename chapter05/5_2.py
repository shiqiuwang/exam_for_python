import math


def isPrime(number: int) -> bool:
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                break
            else:
                return True
        return False


if __name__ == '__main__':
    number = eval(input("请输入一个大于0的整数："))
    while True:
        if type(number) != int:
            number = eval(input("您输入的不是整数，请输入一个整数:"))
        elif number <= 0:
            number = eval(input("您输入的数小于0，请输入一个大于0的整数"))
        else:
            break

    ret = isPrime(number)
    print(ret)

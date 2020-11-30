import math


def printPrime():
    for i in range(2, 201):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=' ')


if __name__ == '__main__':
    printPrime()

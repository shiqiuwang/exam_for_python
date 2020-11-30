from typing import List


def duplicationNum(list1: List[int]) -> bool:
    if len(set(list1)) != len(list1):
        return True
    else:
        return False


if __name__ == '__main__':
    list1 = [1, 2, 3, 5, 5, 4, 4, 6, 7]
    ret = duplicationNum(list1)
    print(ret)

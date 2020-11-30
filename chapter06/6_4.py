from typing import List


def duplicationWord(list1: List[int]) -> bool:
    num_fre_dict = dict()
    for num in list1:
        if num in num_fre_dict.keys():
            num_fre_dict[num] += 1
        else:
            num_fre_dict[num] = 1
    for key, val in num_fre_dict.items():
        if val > 1:
            return True
    return False


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    res = duplicationWord(list1)
    print(res)

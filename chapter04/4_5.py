import random

"""
假设车是3号门，1，2号门都是羊
"""
total = 10000
choose_car_no_change_count = 0
choose_car_change_count = 0

for i in range(total):
    guess = random.randint(1, 3)
    # 不更换
    if guess == 3:
        choose_car_no_change_count += 1
    # 更换
    if guess == 1 or guess == 2:
        choose_car_change_count += 1

print("不更换选择时，选中车的概率是：", choose_car_no_change_count / total)
print("更换选择时，选中车的概率是：", choose_car_change_count / total)

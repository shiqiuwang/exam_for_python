import random

choice_list = []

for i in range(48, 58):
    choice_list.append(chr(i))
for j in range(65, 91):
    choice_list.append(chr(j))
for k in range(97, 123):
    choice_list.append(chr(k))

for i in range(10):
    password = ''
    for j in range(8):
        password += random.choice(choice_list)
    print(password)

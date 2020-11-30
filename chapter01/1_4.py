hobbies = []
for i in range(3):
    s = input('请输入你的小爱好（最多三个，按Q或q结束）：')
    if s.upper() == 'Q':
        break
    hobbies.append(s)

print('你的小爱好是：', ' '.join(hobbies))

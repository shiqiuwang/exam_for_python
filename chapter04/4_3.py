sen = input("请输入一行字符串:")
eng_char_count = 0
num_count = 0
space_count = 0
other_count = 0
for ch in sen:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        eng_char_count += 1
    elif '0' < ch < '9':
        num_count += 1
    elif ch == ' ':
        space_count += 1
    else:
        other_count += 1

print("这一行字符串中的英文字符个数为：{},数字个数为：{},空格个数为：{},其他字符为：{}"
      .format(eng_char_count, num_count, space_count, other_count))

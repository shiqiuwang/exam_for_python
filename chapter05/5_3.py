def compute(string: str):
    eng_char_count = 0
    num_count = 0
    space_count = 0
    other_count = 0
    for ch in string:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            eng_char_count += 1
        elif '0' < ch < '9':
            num_count += 1
        elif ch == ' ':
            space_count += 1
        else:
            other_count += 1

    print("这一行字符串中的英文字符个数为：{},数字个数为：{},空格个数为：{},其他字符为：{}"
          .format(eng_char_count, num_count, space_count, other_count))


if __name__ == '__main__':
    string = "www12345@  op"
    compute(string)

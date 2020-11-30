string_number = input("请输入一个5位数字：")
if string_number == string_number[::-1]:
    print("输入的这个数字是回文数")
else:
    print("输入的这个数字不是回文数")

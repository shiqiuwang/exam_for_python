def static_word_nums(file, ch: str) -> int:
    count = 0
    with open(file=file, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            for letter in line:
                if letter == ch:
                    count += 1

    return count


if __name__ == '__main__':
    file = 'G:\\pycharm_project\\exam\\chapter07\\test1'
    letter = 'd'
    ret = static_word_nums(file, letter)
    print(ret)

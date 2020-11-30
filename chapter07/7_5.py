with open(file='../chapter07/test5', mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    with open(file='../chapter07/letter.csv', mode='w', encoding='utf-8') as f2:
        for line in lines:
            word_list = line.split(',')
            f2.write(','.join(word_list))




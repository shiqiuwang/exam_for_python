def convert_letter(file):
    with open(file=file, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            for letter in line:
                if 'a' <= letter <= 'z':
                    f.write(letter.upper())
                elif 'A' <= letter <= 'Z':
                    f.write(letter.lower())
                else:
                    f.write(letter)


if __name__ == '__main__':
    file = '../chapter07/test2'
    convert_letter(file)

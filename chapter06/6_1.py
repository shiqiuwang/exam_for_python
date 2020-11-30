def wordFre(string: str) -> dict:
    fre_dict = dict()

    for ch in string:
        if ch in fre_dict.keys():
            fre_dict[ch] += 1
        else:
            fre_dict[ch] = 1
    sort_fre_dict = dict(sorted(fre_dict.items(), key=lambda d: d[1], reverse=False))
    return sort_fre_dict


if __name__ == '__main__':
    string = "aabbccdeeee"
    res = wordFre(string)
    print(res)

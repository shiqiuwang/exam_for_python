import jieba

res = jieba.cut('Python是最有意思的编程语言')
print(list(res))

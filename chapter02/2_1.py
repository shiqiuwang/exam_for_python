N = input('请输入一个整数N:')
N = int(N)
res = 1
for i in range(32):
    res *= N
print('N的32次方是', res)

n = int(input())
nguoc = 0
if n < 100 or n > 999:
    print('không phải số có 3 chữ số:')
else:
    while n > 0 :
        cuoi = n % 10
        nguoc = nguoc*10 + cuoi
        n = n // 10
    print(nguoc)
a,b,c = map(float, input().split())
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    if a == b and b == c:
        loai = 'Đều'
    elif a == b or b == c or a == c:
        loai = 'Cân'
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        loai = 'Vuông'
    else:
        loai = 'Thường'
    print(loai,p*2,s)
else:
    print("Khong phai 3 canh cua tam giac")
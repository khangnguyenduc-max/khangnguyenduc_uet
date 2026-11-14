a, b, m, c, d, n = map(float, input().split())
if a * d - b * c != 0:
    print("x =", (m * d - b * n) / (a * d - b * c))
    print("y =", (a * n - m * c) / (a * d - b * c))
elif m * d - b * n == 0 and a * n - m * c == 0:
    print("He co vo so nghiem")
else:
    print("He vo nghiem")
x = float(input())
t = int(x)
if t == x:
    len_ = xuong = gan = t
elif x > 0:
    len_ = t + 1
    xuong = t
    gan = t + 1 if x - t >= 0.5 else t
else:
    len_ = t
    xuong = t - 1
    gan = t - 1 if t - x > 0.5 else t
print(len_, xuong, gan)
m,n = map(int,input().split())
len_ = m // n + (1 if m % n != 0 else 0)
print (len_)
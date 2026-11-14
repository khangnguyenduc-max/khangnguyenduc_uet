c = input()
if 'A' <=c<= 'Z':
    print(chr(ord(c) + 32))
else:
    print(chr(ord(c) - 32))
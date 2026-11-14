ten = input("Ten chu ho: ")
cu = int(input("Chi so thang truoc: "))
moi = int(input("Chi so thang nay: "))

kwh = moi - cu
tien = 0

if kwh > 400:
    tien += (kwh - 400) * 3460
    kwh = 400
if kwh > 300:
    tien += (kwh - 300) * 3350
    kwh = 300
if kwh > 200:
    tien += (kwh - 200) * 2998
    kwh = 200
if kwh > 100:
    tien += (kwh - 100) * 2380
    kwh = 100
if kwh > 50:
    tien += (kwh - 50) * 2050
    kwh = 50
tien += kwh * 1984

print(f"Ho va ten: {ten}")
print(f"Tien phai tra la: {round(tien * 1.08)}")
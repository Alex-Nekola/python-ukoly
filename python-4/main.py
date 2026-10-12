xb=int(input("zadej souřadnici bodu:"))
yb=int(input("zadej souřadnici bodu:"))

x1_oblast = 5
y1_oblast = 2
x2_oblast = 10
y2_oblast = 7

if xb>=x1_oblast and xb<=x2_oblast and yb>=y1_oblast and yb<=y2_oblast:
    print ("nepatří")
else:
    print ("patří")

lezi_na_1 = xb>=x1_oblast and xb<=x2_oblast and yb==y1_oblast
lezi_na_2 = yb>=x1_oblast and yb<=x2_oblast and xb==x2_oblast
lezi_na_3 = xb>=y1_oblast and xb<=y2_oblast and yb==y2_oblast
lezi_na_4 = yb>=y1_oblast and yb<=y2_oblast and xb==x1_oblast


if lezi_na_1 or lezi_na_2 or lezi_na_3 or lezi_na_4:
    print("bod leží na hranici")
else:
    print("bod leží mimohranici")



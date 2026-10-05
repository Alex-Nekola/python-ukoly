# příkaz větvení
x = 0
a = x

if x > 0:
    print("kladné")
else:
    if (x<0):
        print("záporné")
        a = -x
    else:
        print("nula")
# sem směřují skoky ze všech větví příkazu if

print(f"absolutní hodnota čísla {x} je {a}")

if x>0:
    print("kladné")
elif x<0:
    print("záporné")
    a = -x
else:
    print("nula")

    
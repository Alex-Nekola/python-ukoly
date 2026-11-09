import math
print("Je zadané číslo prvočíslem?")
cislo = int(input("zadejte celéčíslo: "))

je_prvocislo = True

if cislo<2:
    je_prvocislo = False
elif cislo == 2:
    je_prvocislo = True
elif cislo % 2 == 0:
    je_prvocislo = False
else:
    delitel = 3
    while delitel<math.sqrt(cislo):
        if cislo % delitel == 0:
            je_prvocislo = False
            break
        delitel += 2

if je_prvocislo:
    print (f"cislo {cislo} JE prvočíslo")
else:
    print (f"cislo {cislo} NENÍ prvočíslo")

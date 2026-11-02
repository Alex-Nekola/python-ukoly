import random
tajne_cislo = random.randint(1,20)
tip = 0
pokusy = 0

print("Myslím si číslo od 1 do 20.")
while tip != tajne_cislo:
    tip=int(input("zadej tip "))
    pokusy += 1
    if tip > tajne_cislo:
     print("myslim si menší číslo")
    elif tip < tajne_cislo:
     print("myslim si větší číslo")
     if tip <1:
      print("zadej platné číslo")
      pokusy -= 1
      if tip >20:
            print("zadej platné číslo")
            pokusy -= 1
    if pokusy == 5:
     break

if tip == tajne_cislo:
 print(f"Správně, uhádl jsi moje číslo {tajne_cislo} do {pokusy} pokusů")
else: print("Neuhádls číslo do 5 pokusů")

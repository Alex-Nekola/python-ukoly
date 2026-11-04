print("Mysli si číslo a já ho do 7 tipů uhodnu")
dole = 1
nahore = 100
pokusy=0


while dole <= nahore:
    tip= (dole + nahore) //2
    pokusy += 1

    print (f"muj tip je {tip}")
    odpoved= input("je to správně(=), je tvé číslo větší (>) nebo menší (<)")

    if odpoved == "=":
     print (f"uhodl jsem ho za {pokusy } pokusů")
     break
    elif odpoved == ">":
     dole = tip + 1
    elif odpoved == "<":
     nahore = tip - 1
    else:
      print("neplatná hodnota")
      pokusy -= 1
else:
  print("Prohrál jsem asi jsi někde udělal chybu")
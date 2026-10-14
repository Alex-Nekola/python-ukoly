c = 500
x = int(input("počet lidí: "))

if x>=4:
  cena=c*x*0.75
else:
  p=int(input("věk? "))
  if p>=65:
    cena=c*x*0.8
  elif p<26:
    s = input("Student? [ano/ne]")
  elif s=="ano":
    cena=c*x*0.7
  else:
   cena=c*x

print(f"cena vstupenky:", cena / x)
print("cena celková")

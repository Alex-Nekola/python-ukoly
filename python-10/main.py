# funkce pro výpočet obsahu obdelníku
def spocitej_obsah(a, b):
    # kontrola platnosti zadaných délek
    if a <= 0 or b <= 0:
        return None
    obsah = a* b
    return obsah
#   return a * b

# ---hlavní kod programu---

print("VÝPOČET ROZLOHY BYTU")
pocet_mistnosti = int(input("Zadej počet místností: "))
mistnost = 1
obsah = 0  # proměnná pro celkovou výměru bytu 
while mistnost <= pocet_mistnosti:
    print(f"Zadej rozměry {mistnost}. mistnosti")
    a = int(input("zadej stranu 'a':"))
#   a = int(input("zadej stranu \"a\":")) 
    b = int(input("zadej stranu \"b\":"))
    obsah += spocitej_obsah(a, b)
    mistnost += 1
print(f"Celková výměra bytu je {obsah}")



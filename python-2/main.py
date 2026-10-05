# *********************************
# Kalkulačka spropitného
# 30.9.2026 
# *********************************

print("Kalkulačka spropitného")  # titulní text
celkova_cena = float(input("Zadej celkovou cenu: "))
spropitne = int(input("Zadej spropitné v %: "))
pocet_lidi = int(input("Zadej počet lidí: "))

# celkova_cena = celkova_cena + celkova_cena * spropitne / 100 # aritmeticé operace +,-,*,/
# celkova_cena = celkova_cena * (1 + spropitne / 100)
celkova_cena += celkova_cena * spropitne / 100
uhradit = round(celkova_cena / pocet_lidi)

print(f"celkova_cena {celkova_cena} dělená {pocet_lidi} je {uhradit}")


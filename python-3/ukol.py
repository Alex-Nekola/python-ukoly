x = float(input("zadej čas: "))

if x<0:
    print("Hodina nemůže být záporná")
elif x>24:
    print("Zadavejte platne hodiny")
elif x<6:
    print("Je noc")
elif x<10:
    print("Je ráno")
elif x<12:
    print("Je dopoledne")
elif x<19:
    print("Je odpoledne")
elif x>18:
    print("Je noc")

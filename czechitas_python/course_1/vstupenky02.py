print("Divadlo Pěst na oko")
print("Vítejte v online rezervaci vstupenek")
print("Pro vstup do systému je potřeba registrace")
uzivatel = input("Uveďte své uživatelské jméno: ")
vek = int(input("Uveďte svůj věk: "))
plna_cena = 12
if vek < 6:
    cena = 0
elif vek <= 26:
    cena = plna_cena / 100 * 65
elif vek <= 64:
    cena = plna_cena
else:
    cena = plna_cena / 2
cena = round(cena, 2)
print(f"Cena vstupenky je {cena} eur. Uzijte si divadelni predstaveni.")
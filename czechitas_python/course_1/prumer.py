cisla = [2.45, 8.3, 4.55, 9.54, 7.43]
soucet = 0
for cislo in cisla:
    soucet += cislo
print(f"Soucet vsech polozek: {soucet}")

pocet_polozek = len(cisla)
print(f"Pocet polozek: {pocet_polozek}")
prumer = soucet/pocet_polozek
print(f"Prumer: {prumer}")
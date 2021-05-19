cisla = [5, -4, -10, 7, 14, 2, 49, 76, 21]
cisla = [1,2,3,4,5]
nejvyssi_cislo = cisla[0]
for cislo in cisla:
    if cislo > nejvyssi_cislo:
        nejvyssi_cislo = cislo
print(nejvyssi_cislo)

nejmensi_cislo = cisla[0]
for cislo in cisla:
    if cislo < 0:
        nejmensi_cislo = cislo
print(nejmensi_cislo)
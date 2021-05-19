import random

dolni_mez = int(input("Dolni mez: "))
horni_mez = int(input("horni mez: "))
nahodne_cislo = random.randint(dolni_mez, horni_mez)
print(nahodne_cislo)
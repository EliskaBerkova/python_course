"""
Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. Hostu na seznamu, který zadá správné heslo, vypíše program text: “Smíš vstoupit.”
"""
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

jmeno = input("Tve jmeno: ")
if jmeno in passwords:
    heslo = input("Vloz heslo: ")
    if heslo in passwords[jmeno]:
        print("Smis vstoupit")
    else:
        print("Spatne heslo")
else:
    print("Nejsi na seznamu")
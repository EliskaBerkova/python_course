jmeno = input("Uvedte sve uzivatelske jmeno: ")
heslo = input("Uvedte heslo: ").lower()

if heslo == "simsalabim":
    vek = int(input("Zadej vek: "))
    if vek >= 18:
        print("Smis vstoupit")
    else:
        exit()
else:
    print("Vstup nepovolen")
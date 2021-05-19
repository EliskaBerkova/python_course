jmeno = "Eliska Berkova"
print(jmeno[2], jmeno[4], jmeno[6])

email = input("Vlozte svuj email: ")
delka = len(email)
print(delka)
#if "@" in email and "." in email and delka >=5 :
#    print("Vse je v poradku.")
#else:
#    print("Chybny email")

if "@" in email:
    if "." in email:
        if delka >= 5:
            print("Email je OK")
        else:
            print("Email je kratky")
    else:
        print("Chybi tecka")
else:
    print("Chybi zavinac")
vek = input("Zadej věk: ")
vek = int(vek)
if vek >= 18:
    obcanka = input("Mate obcansky prukaz ano/ne? ").lower()
    if obcanka == "ano":
        print("Nabídka her pro dospělé")
    else:
        print("Je potreba predlozit obcansky prukaz.")
else:
    print("Hry pro dospělé nejsou zobrazeny")
print("Nabídka her pro děti")

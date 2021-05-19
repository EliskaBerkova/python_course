tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

cislo_listku = int(input("Vloz cislo listku: "))


if cislo_listku in tombola:
    vyhra = tombola[cislo_listku]
    print(f"Vyhravas {vyhra}")
    tombola.pop(cislo_listku)
else:
    print("Bohužel nevyhráváš nic.")
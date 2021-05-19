item = {
    "title": "Čajová konvička s hrnky",
    "price": 899,
    "in_stock": True,
}

item["price"] = 950
title = item["title"]
price = item["price"]
item["weight"] = 0.4


print(f"Nazev polozky je: {title} a cena je {price} Kc.")

if "weight" in item:
    print(f"Hmotnost predmetu je: {item['weight']} kg.")
else:
    print("Hmotnost neni zadana.")


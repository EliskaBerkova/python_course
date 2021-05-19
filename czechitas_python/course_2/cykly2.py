books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

total = 0
for item in books:
    total += item["sold"]
print(f"Celkovy pocet prodanych kusu: {total}")

total2 = 0
for item in books:
    if item["price"] > 300:
        trzba = item["sold"] * item["price"]
        total2 += trzba
print(f"Celkova trzba za knihy drazsi nez 300 Kc: {total2}")


sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

for kniha in sales:
    print(kniha)

total = 0

for key, value in sales.items():
    total += value
    print(f"Knihu '{key}' jsme prodali v poctu {value} kusu.")
print(f"Celkove jsme prodali: {total} kusu")


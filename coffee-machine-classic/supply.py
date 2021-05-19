MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# def compare_price(inserted, price):
#     if inserted > price:
#         return "too much"
#     elif inserted == price:
#         return "enough"
#     else:
#         return "not enough"


#print(compare_price(inserted_coins, item_price))

# vypsani vsech polozek v menu a jejich ingredienci
# hranate zavorky se daji retezit, napr MENU['espresso']['ingredients']['water']

# for item in MENU:
#     print(f"{item}: {MENU[item]}")
#     print(f"{item} ingredients: {MENU[item]['ingredients']}")

# kdyz v ingrediencich pro espresso neexistuje klic mleko, pridam ho s hodnotou nula, abych pak nedostal KeyError
if "milk" not in MENU["espresso"]["ingredients"]:
    MENU["espresso"]["ingredients"]["milk"] = 0
print(MENU["espresso"]["ingredients"]["milk"])
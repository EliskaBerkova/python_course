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

from art import logo
def compare_price(inserted, price):
    if inserted > price:
        return "too much"
    elif inserted == price:
        return "equal"
    else:
        return "not enough"


def enough_ingredients(item, resource):
    if item < resource:
        return True
    else:
        return False


# kdyz v ingrediencich neexistuje klic mleko, pridam ho s hodnotou nula, abych nedostala KeyError:
for item in MENU:
    if "milk" not in MENU[item]["ingredients"]:
        MENU[item]["ingredients"]["milk"] = 0

# objednavka
order = ''
profit = 0
print(logo)
while order != "off":
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        print(f"Water:{resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")

    elif order == "service":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
    elif order == "off":
        pass
    elif order not in MENU:
        print("That's not an option, dumbass")
    else:
        item = MENU[order]
        item_ingredients = item["ingredients"]
        water = item_ingredients["water"]
        milk = item_ingredients["milk"]
        coffee = item_ingredients["coffee"]
        item_price = item["cost"]

        # kontrola dostatku ingredienci
        enough_water = enough_ingredients(water, resources["water"])
        enough_coffee = enough_ingredients(coffee, resources["coffee"])
        enough_milk = enough_ingredients(milk, resources["milk"])


        if not enough_water and not enough_coffee:
            print(f"Sorry, there is not enough water and coffee. Call service.")
        elif not enough_milk and not enough_coffee:
            print(f"Sorry, there is not enough milk and coffee. Call service.")
        elif not enough_water and not enough_milk:
            print(f"Sorry, there is not enough water and milk. Call service.")
        elif not enough_water:
            print(f"Sorry, there is not enough water. Call service.")
        elif not enough_coffee:
            print(f"Sorry, there is not enough coffee. Call service.")
        elif not enough_milk:
            print(f"Sorry, there is not enough milk. Call service.")



        if enough_water and enough_coffee and enough_milk:
            # vypsani castky
            print(f"The price of {order} is: ${item_price}")

            # mince
            print("Please, insert coins.")
            quarters = int(input("  how many quarters? "))
            dimes = int(input("  how many dimes? "))
            nickles = int(input("  how many nickles? "))
            pennies = int(input("  how many pennies? "))

            inserted_coins = round(((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)), 2)
            # print(inserted_coins)
            # print(item_price)

            result = compare_price(inserted_coins, item_price)

            change = 0
            if result == "too much":
                change = inserted_coins - item_price
                print(f"Here is ${change} in change.\nHere is your {order} ☕ Enjoy.")
            elif result == "equal":
                print(f"Here is your {order} ☕ Enjoy.")
            elif result == "not enough":
                print("Sorry, that's not enough money. Money refunded.")


            if result != "not enough":
                resources["water"] = resources["water"] - water
                resources["milk"] = resources["milk"] - milk
                resources["coffee"] = resources["coffee"] - coffee

                profit = profit + item_price

# if order == "espresso":
#     #check_resources
# elif order == "latte":
#     #check_resources
# elif order == "cappuccino":
#     # check_resources
# elif order == "report":
#     # vypise zbyvajici zdroje
# elif order == "off":
#     # ukonci program
# else:
#     print("There is no possibility like this.")
#     # vratit na zacatek


# objednavka
# kontrola zdroju
    #pokud je zdroju dostatek, pokracovat dal
    #pokud je zdroju nedostatek, znovu pokracovat od zacatku
# vypsani castky




# pokud je castka v poradku, vratit drobne
    # pokud je castka nizsi, vypsat, ze penize nestaci
# vyrobit kavu => ponizit resources
# znovu zacit od zacatku






# poznamky/stare veci
# def enough_water(item, water_resources):
#     if item < water_resources:
#         remaining_water = water_resources - item
#         return remaining_water
#
# def enough_coffee(item, coffee_resources):
#     if item < coffee_resources:
#         remaining_coffee = coffee_resources - item
#         return remaining_coffee
#
# def enough_milk(item, milk_resources):
#     if item < milk_resources:
#         remaining_milk = milk_resources - item
#         return remaining_milk
#
#
# resources["water"] = enough_water(water, resources["water"])
# resources["milk"] = enough_milk(milk, resources["milk"])
# resources["coffee"] = enough_coffee(coffee, resources["coffee"])
#
# print(resources["water"])
# print(resources["milk"])
# print(resources["coffee"])



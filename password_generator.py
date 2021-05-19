# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

# do range uvedu kolikrat ma vybrat uvedene pismeno, protoze posledni cislo v rozsahu uvedenem v zavorce neni, musim pricist 1

for char in range(1, nr_letters + 1):
    # nasledujici krok se postupne vybiraji jednotliva pismena a skladaji se za sebe
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(f"Your password with not randomised order is: {password}\n")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# v pripade, kdy ma byt nahodne i poradi hesla, je nutne si vytvorit <list>
password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# print(password_list)

# poradi symbolu, pismen a cisel zmenim nasledovne:
random.shuffle(password_list)
# print(password_list)

# takto vypisu cele heslo za sebou:
password = ""
for char in password_list:
    password += char

print(f"Your password with randomised order is: {password}")

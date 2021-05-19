data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
]
score = 0

import random

def get_choice(choice):
    return f"{choice['name']}, a {choice['description']}, from {choice['country']}"

# porovnat hodnoty poctu followeru mezi sebou, urcit vyssi
def compare_followers(choice_x, choice_y):
    if choice_x["follower_count"] > choice_y["follower_count"]:
        return choice_x
    else:
        return choice_y

def guess_vs_winner(g, w):
    if g == w:
        return f"You are right."
    else:
        return f"Sorry, that's wrong."


# nahodny vyber obou polozek
choice_A = random.choice(data)


end_game = False
while end_game == False:
    choice_B = random.choice(data)

    # vybirat choice B dokud se nebude lisit od A
    while choice_A == choice_B:
        choice_B = random.choice(data)

    print(f"Compare A: {get_choice(choice_A)}")
    # print(vs)
    print(f"Against B: {get_choice(choice_B)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if guess == "a":
        guess = choice_A
        # print(guess)
    elif guess == "b":
        guess = choice_B
        # print(guess)
    else:
        print(f"There's no possibility like '{(guess).upper()}'")

    # porovnani poctu followeru vybranych polozek
    winner = compare_followers(choice_A, choice_B)
    # print(winner)

    # porovnani followeru z meho tipu s followery viteze


    if guess_vs_winner(guess, winner) == "You are right.":
        # pokud muj tip spravny, ulozim do choice A
        choice_A = winner
        # v pripade, ze je muj tip spravny +1 bod
        score += 1
    else:
        # pokud je muj tip spatny, konec hry
        end_game = True
    print(f'{guess_vs_winner(guess, winner)} Current score: {score}\n')
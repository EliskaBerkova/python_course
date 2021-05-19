import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    random_card = random.choice(cards)
    return random_card

deal_card()

def calculate_score(hand_cards):
    score = sum(hand_cards)
    if (11 in hand_cards) and score > 21:
        score -= 10
    return score

def has_blackjack(hand_cards):
    if len(hand_cards) == 2 and sum(hand_cards) == 21:
        return True
    else:
        return False

def who_won(x, y):
    if x > y:
        return f"Your final hand: {user_cards}, final score: {user_score}\nComputer final hand: {computer_cards}, final score: {computer_score}\nYou win."
    elif x < y:
        return f"Your final hand: {user_cards}, final score: {user_score}\nComputer final hand: {computer_cards}, final score: {computer_score}\nYou lose."
    else:
        return f"Your final hand: {user_cards}, final score: {user_score}\nComputer final hand: {computer_cards}, final score: {computer_score}\nIt's a draw."

#print(f'user cards: {user_cards}, user score: {user_score}')


start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n'. ")
if start_game == "y":
    user_cards = []
    computer_cards = []
    ended = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score} ")
    #print(f"Computer cards: {computer_cards}, current score: {computer_score} ")
    print(f"Computer's first card: {computer_cards[0]}")

    if has_blackjack(user_cards):
        print("You win.")
        ended = True
    if has_blackjack(computer_cards):
        print("You lose.")
        ended = True

    another_card = 'y'

    while another_card == 'y' and not ended:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            user_cards.append(deal_card())
        user_score = calculate_score(user_cards)

        if user_score > 21:
            ended = True

        print(f"Your cards: {user_cards}, current score: {user_score} ")
        print(f"Computer's first card: {computer_cards[0]}")

    if user_score > 21:
        print(f"Your final hand: {user_cards}, final score: {user_score}\nComputer final hand: {computer_cards}, final score: {computer_score}\nYou lose.")
    else:
        # computer plays
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        #print(f"Computer cards: {computer_cards}")
        if computer_score > 21:
            print(f"Your final hand: {user_cards}, final score: {user_score}\nComputer final hand: {computer_cards}, final score: {computer_score}\nOpponent went over. You win.")
        else:
            print(who_won(user_score, computer_score))
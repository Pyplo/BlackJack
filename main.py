from art import logo
import random


def take_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card


def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_decks(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        print("You went over. You Lose!")

    if user_score == computer_score:
        return "Draw!"
    elif user_score == 0:
        return "BlackJack! You Win"
    elif computer_score == 0:
        return "Computer has BlackJack! You Lose"
    elif user_score > 21:
        return "You went over. You Lose"
    elif computer_score > 21:
        return "Opponent went over. You Lose"
    elif user_score > computer_score:
        return "You Win!"
    elif user_score < computer_score:
        return "You Lose!"
    else:
        return "You Lose!"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for x in range(2):
        user_cards.append(take_card())
        computer_cards.append(take_card())
    while not is_game_over:
        user_score = calculate(user_cards)
        computer_score = calculate(computer_cards)
        print(f"Your cards: {user_cards}, current score {user_score} \n"
              f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(take_card())
            else:
                is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(take_card())
            computer_score = calculate(computer_cards)

    print(f"Your Final hand: {user_cards}, final score: {user_score} \n"
          f"Computer's Final hand: {computer_cards}, final score: {computer_score}")
    print(compare_decks(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    play_game()

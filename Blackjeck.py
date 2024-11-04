import random

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

def draw():
    keys_card = list(cards.keys())
    return random.choice(keys_card)

def score(hand):
    total = sum(cards[card] for card in hand)
    if total > 21 and "A" in hand:
        total -= 10 * hand.count("A")
    return total

def show(player,dealer,msg):
    print(f"\nYour cards: ")
    for card in player: print(card)
    print(f"Your score: {score(player)} \n{msg}")
    for card in dealer: print(card)

def is_message(msg):
    while True:
        user_input = input(msg).lower()
        print("=====  =====")
        if user_input in {"y","n"}: return user_input == "y"

def play_round():
    player, dealer = ["A","A"], [draw(), draw()]
    if score(dealer) == 21:
        show(player,dealer,"Dealer's cards: ")
        return print("Dealer has Blackjack, you lose.")

    while score(player) < 22:
        show(player,[dealer[0]],"Dealer's first card: ")
        if score(player) == 21:
            return print("Blackjack, you win!")
        if not is_message("Type y to draw any card or type n to pass: "):
            break
        player.append(draw())

    if score(player) > 21:
        show(player,[dealer[0]],"Dealer's first card: ")
        return print("Bust!, you lose.")

    while score(dealer) < 17:
        dealer.append(draw())

    show(player,dealer,"Dealer's cards: ")
    print(f"Your final score: {score(player)}, dealer's final score: {score(dealer)}")
    if score(dealer) > 21 or score(dealer) < score(player):
        return print("You win!")
    if score(dealer) > score(player):
        return print("You lose.")
    print("It's a draw!")

def blackjack():
    print("Wellcome to Blackjack")
    if not is_message("Are you ready to play game? [y/n]: "): return
    while True:
        play_round()
        if not is_message("Do you want to play again? [y/n]: "):
            break
    print("Thank you for supporting...")

blackjack()
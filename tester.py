import random


cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}


def draw_card(): return random.choice(list(cards.keys()))


def score(hand): return sum(cards[c] for c in hand) - 10 * hand.count("A") if sum(cards[c] for c in hand) > 21 and "A" in hand else sum(cards[c] for c in hand)


def is_message(msg):
    while (response := input(msg).lower()) not in {"y","n"}:pass
    return response == "y"


def show_cards(player, dealer, smg): return print(f"\nYour cards: \n{"\n".join(player)}\nYour score: {score(player)}\n{smg}\n{"\n".join(dealer)}")


def play_round():
    player, dealer = [draw_card(), draw_card()], [draw_card(), draw_card()]
    if score(dealer) == 21: return show_cards(player, dealer, "Dealer's cards: "), print("Dealer has Blackjack, you lose.")
    if score(player) == 21: return show_cards(player, [dealer[0]], "Dealer's first card: "), print("Blackjack, you win!")
    while score(player) < 22:
        show_cards(player, [dealer[0]], "Dealer's first card: ")
        if not is_message("Type y to draw any card or type n to pass: "): break
        player.append(draw_card())
    if score(player) > 21: return show_cards(player, [dealer[0]], "Dealer's first card: "), print("Bust! you lose.")
    while score(dealer) < 17: dealer.append(draw_card())
    show_cards(player, dealer, "Dealer's cards: ")
    print(f"Your final score: {score(player)}, dealer's final score: {score(dealer)}")
    if score(player) > score(dealer): return print("You win!")
    print("You lose.") if score(dealer) > score(player) else print("It's a draw!")


def start_game():
    print("Wellcome to Blackjack")
    if not is_message("Are you ready to play game? [y/n]: "): return
    while True:
        play_round()
        if not is_message("Do you want to play again? [y/n]: "): return


start_game()
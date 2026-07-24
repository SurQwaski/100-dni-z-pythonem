import random
import assets

card_deck = {"2" : 2,
             "3" : 3,
             "4" : 4,
             "5" : 5,
             "6" : 6,
             "7" : 7,
             "8" : 8,
             "9" : 9,
             "10" : 10,
             "J" : 10,
             "Q" : 10,
             "K" : 10,
             "A" : 11,}

card_suits = ["♠","♥","♣","♦"]

def deal_card():
    dealt_card = (random.choice(list(card_deck.items())))
    return dealt_card

def calculate_score(current_hand):
    current_score = 0
    Ace_in_hand = False
    Ace_count = 0
    for card in current_hand:
        current_score += card[1]
        if card[0] == "A":
            Ace_in_hand = True
            Ace_count += 1

    if Ace_in_hand and current_score > 21:
        for _ in range(Ace_count):
            current_score -= 10
            if current_score <= 21:
                break
    return current_score

def display_current_hand(current_hand, display_hand):
    if len(display_hand) == 0:
        for card in current_hand:
            display_hand.append(card[0] + random.choice(card_suits))
        return display_hand
    else:
        display_hand.append(current_hand[-1][0] + random.choice(card_suits))
        return display_hand

def blackjack():
    print(assets.BLACKJACK_LOGO)
    print(assets.WELCOME_MESSAGE)

    game_over = False
    dealer_hand = []
    player_hand = []
    dealer_display_hand = []
    player_display_hand = []

    for _ in range(2):
        dealer_hand.append(deal_card())
        player_hand.append(deal_card())

    player_display_hand = display_current_hand(player_hand,player_display_hand)
    dealer_display_hand = display_current_hand(dealer_hand, dealer_display_hand)

    while not game_over:
        print(f"Your cards: {' '.join(player_display_hand)} Current score: {calculate_score(player_hand)}")
        print(f"Computer's first card: {dealer_display_hand[0]}")

        decision = input("Type 'h' to hit, 's' to stand. ").lower()

        if decision == "h":
            player_hand.append(deal_card())
            player_display_hand = display_current_hand(player_hand,player_display_hand)
            if calculate_score(player_hand) > 21:
                print("Bust!")
                print(f"Computer's hand was: {' '.join(dealer_display_hand)}")
                game_over = True
        elif decision == "s":
            game_over = True
            dealers_turn = True
            while dealers_turn:
                if calculate_score(dealer_hand) < 17:
                    dealer_hand.append(deal_card())
                    dealer_display_hand = display_current_hand(dealer_hand,dealer_display_hand)
                else:
                    if calculate_score(dealer_hand) > 21:
                        print(f"Dealer Busted! Dealer's final hand: {' '.join(dealer_display_hand)}")
                    elif calculate_score(dealer_hand) > calculate_score(player_hand):
                        print(f"You lose! Dealer's final hand: {' '.join(dealer_display_hand)}")
                    elif calculate_score(dealer_hand) == calculate_score(player_hand):
                        print(f"Draw! Dealer's final hand: {' '.join(dealer_display_hand)}")
                    else:
                        print(f"You win! Dealer's final hand: {' '.join(dealer_display_hand)}")
                    dealers_turn = False
                print(f"Dealer's final score was: {calculate_score(dealer_hand)}")

        else:
            print("Invalid command. Try again.")

blackjack()
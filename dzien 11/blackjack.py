import random
from assets import card_deck, card_suits, BLACKJACK_LOGO, WELCOME_MESSAGE

def deal_card(hand, times):
    for _ in range(times):
        dealt_card = (random.choice(list(card_deck.items())))
        hand.append(dealt_card)

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

def display_current_hand(current_hand, display_hand, first_card_only):
    if len(display_hand) == 0:
        for card in current_hand:
            display_hand.append(card[0] + random.choice(card_suits))
    elif len(current_hand) != len(display_hand):
        diff = len(current_hand) - len(display_hand)
        for i in reversed(range(1,diff+1)):
            display_hand.append(current_hand[-i][0] + random.choice(card_suits))
    else:
        pass

    if not first_card_only:
        return(" ".join(display_hand))
    else:
        return(display_hand[0])

def blackjack():
    print(BLACKJACK_LOGO)
    print(WELCOME_MESSAGE)

    game_over = False
    dealer_hand = []
    player_hand = []
    dealer_display = []
    player_display = []

    deal_card(hand=dealer_hand, times=2)
    deal_card(hand=player_hand, times=2)

    while not game_over:
        print(f"Your cards: {display_current_hand(current_hand=player_hand, display_hand=player_display, first_card_only=False)}")
        print(f"Current score: {calculate_score(player_hand)}")
        print(f"Computer's first card: {display_current_hand(current_hand=dealer_hand,display_hand=dealer_display, first_card_only=True)}")

        decision = input("Type 'h' to hit, 's' to stand. ").lower()

        if decision == "h":
            deal_card(hand=player_hand, times=1)
            if calculate_score(player_hand) > 21:
                print("Bust!")
                print(f"Computer's hand was: {display_current_hand(current_hand=dealer_hand, display_hand=dealer_display, first_card_only=False)}")
                game_over = True
        elif decision == "s":
            game_over = True
            dealers_turn = True
            while dealers_turn:
                if calculate_score(dealer_hand) < 17:
                    deal_card(hand=dealer_hand, times=1)
                else:
                    if calculate_score(dealer_hand) > 21:
                        print(f"Dealer Busted! Dealer's final hand: {display_current_hand(current_hand=dealer_hand,display_hand=dealer_display,first_card_only=False)}")
                    elif calculate_score(dealer_hand) > calculate_score(player_hand):
                        print(f"You lose! Dealer's final hand: {display_current_hand(current_hand=dealer_hand,display_hand=dealer_display,first_card_only=False)}")
                    elif calculate_score(dealer_hand) == calculate_score(player_hand):
                        print(f"Draw! Dealer's final hand: {display_current_hand(current_hand=dealer_hand,display_hand=dealer_display,first_card_only=False)}")
                    else:
                        print(f"You win! Dealer's final hand: {display_current_hand(current_hand=dealer_hand,display_hand=dealer_display,first_card_only=False)}")
                    dealers_turn = False
            print(f"Dealer's final score was: {calculate_score(dealer_hand)}")
        else:
            print("Invalid command. Try again.")

blackjack()
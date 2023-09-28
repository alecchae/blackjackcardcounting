from Deck import Deck
from Player import Player


def display_hand(player):
    print(f"{player.name}'s hand:")
    for card in player.hand:
        print(card)


# Initialize the deck and shuffle it
deck = Deck()
deck.shuffle()

# Initialize the player and dealer
player = Player("Player")
dealer = Player("Dealer")

# Deal the initial cards
for _ in range(2):
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

# Main game loop
for i in range(int(input("number for shoe games : "))):
    while deck.count < 29:
        # Display player's hand and current score
        display_hand(player)
        display_hand(dealer)
        player_score = player.calculate_score()
        print(f"Score: {player_score}")

        # Check for a player blackjack (21)
        if player_score == 21:
            print("Blackjack! You win!")
            break

        # Ask the player if they want to hit or stand
        choice = input("Do you want to 'hit' or 'stand'? ").lower()
        if choice == 'hit':
            player.add_card(deck.deal_card())
        elif choice == 'stand':
            break

    # Dealer's turn
    while dealer.calculate_score() < 17:
        dealer.add_card(deck.deal_card())

    # Display the final hands
    display_hand(player)
    player_score = player.calculate_score()
    print(f"Player Score: {player_score}")
    display_hand(dealer)
    dealer_score = dealer.calculate_score()
    print(f"Dealer Score: {dealer_score}")

    # Determine the winner
    if player_score > 21:
        print("Bust! Dealer wins.")
    elif dealer_score > 21:
        print("Dealer busts! You win.")
    elif player_score > dealer_score:
        print("You win!")
    elif dealer_score > player_score:
        print("Dealer wins.")
    else:
        print("It's a tie!")

    deck.shuffle()

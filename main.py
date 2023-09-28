from Deck import Deck
from Player import Player


def display_hand(player):
    print(f"{player.name}'s hand:")
    for card in player.hand:
        print(card)


# basic strategy chart
basic_strategy_hard_total_chart = {
    8: {'Two': 'H', 'Three': 'H', 'Four': 'H', 'Five': 'H', 'Six': 'H', 'Seven': 'H', 'Eight': 'H', 'Nine': 'H',
        'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    9: {'Two': 'H', 'Three': 'D', 'Four': 'D', 'Five': 'D', 'Six': 'D', 'Seven': 'H', 'Eight': 'H', 'Nine': 'H',
        'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    10: {'Two': 'D', 'Three': 'D', 'Four': 'D', 'Five': 'D', 'Six': 'D', 'Seven': 'D', 'Eight': 'D', 'Nine': 'D',
         'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    11: {'Two': 'D', 'Three': 'D', 'Four': 'D', 'Five': 'D', 'Six': 'D', 'Seven': 'D', 'Eight': 'D', 'Nine': 'D',
         'Ten': 'D', 'Jack': 'D', 'Queen': 'D', 'King': 'D', 'Ace': 'D'},
    12: {'Two': 'H', 'Three': 'H', 'Four': 'S', 'Five': 'S', 'Six': 'S', 'Seven': 'H', 'Eight': 'H', 'Nine': 'H',
         'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    13: {'Two': 'S', 'Three': 'S', 'Four': 'S', 'Five': 'S', 'Six': 'S', 'Seven': 'H', 'Eight': 'H', 'Nine': 'H',
         'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    14: {'Two': 'S', 'Three': 'S', 'Four': 'S', 'Five': 'S', 'Six': 'S', 'Seven': 'H', 'Eight': 'H', 'Nine': 'H',
         'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    15: {'Two': 'S', 'Three': 'S', 'Four': 'S', 'Five': 'S', 'Six': 'S', 'Seven': 'H', 'Eight': 'H', 'Nine': 'H',
         'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    16: {'Two': 'S', 'Three': 'S', 'Four': 'S', 'Five': 'S', 'Six': 'S', 'Seven': 'H', 'Eight': 'H', 'Nine': 'H',
         'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    17: {'Two': 'S', 'Three': 'S', 'Four': 'S', 'Five': 'S', 'Six': 'S', 'Seven': 'S', 'Eight': 'S', 'Nine': 'S',
         'Ten': 'S', 'Jack': 'S', 'Queen': 'S', 'King': 'S', 'Ace': 'S'},
}

basic_strategy_soft_total_chart = {
    {'Ace', 'Nine'}: {'Two': 'S', 'Three': 'S', 'Four': 'S', 'Five': 'S', 'Six': 'S', 'Seven': 'S', 'Eight': 'S',
                      'Nine': 'S',
                      'Ten': 'S', 'Jack': 'S', 'Queen': 'S', 'King': 'S', 'Ace': 'S'},
    {'Ace', 'Eight'}: {'Two': 'S', 'Three': 'S', 'Four': 'S', 'Five': 'S', 'Six': 'S', 'Seven': 'S', 'Eight': 'S',
                       'Nine': 'S',
                       'Ten': 'S', 'Jack': 'S', 'Queen': 'S', 'King': 'S', 'Ace': 'S'},
    {'Ace', 'Seven'}: {'Two': 'S', 'Three': 'S', 'Four': 'S', 'Five': 'S', 'Six': 'S', 'Seven': 'S', 'Eight': 'S',
                       'Nine': 'H',
                       'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    {'Ace', 'Six'}: {'Two': 'H', 'Three': 'H', 'Four': 'H', 'Five': 'H', 'Six': 'H', 'Seven': 'H', 'Eight': 'H',
                     'Nine': 'H',
                     'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    {'Ace', 'Five'}: {'Two': 'H', 'Three': 'H', 'Four': 'H', 'Five': 'H', 'Six': 'H', 'Seven': 'H', 'Eight': 'H',
                      'Nine': 'H',
                      'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    {'Ace', 'Four'}: {'Two': 'H', 'Three': 'H', 'Four': 'H', 'Five': 'H', 'Six': 'H', 'Seven': 'H', 'Eight': 'H',
                      'Nine': 'H',
                      'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    {'Ace', 'Three'}: {'Two': 'H', 'Three': 'H', 'Four': 'H', 'Five': 'H', 'Six': 'H', 'Seven': 'H', 'Eight': 'H',
                       'Nine': 'H',
                       'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
    {'Ace', 'Two'}: {'Two': 'H', 'Three': 'H', 'Four': 'H', 'Five': 'H', 'Six': 'H', 'Seven': 'H', 'Eight': 'H',
                     'Nine': 'H',
                     'Ten': 'H', 'Jack': 'H', 'Queen': 'H', 'King': 'H', 'Ace': 'H'},
}

basic_strategy_pair_splitting_chart = {
    {'Ace', 'Ace'}: {'Two': 'Y', 'Three': 'Y', 'Four': 'Y', 'Five': 'Y', 'Six': 'Y', 'Seven': 'Y', 'Eight': 'Y',
                     'Nine': 'Y',
                     'Ten': 'Y', 'Jack': 'Y', 'Queen': 'Y', 'King': 'Y', 'Ace': 'Y'},
    {'King', 'King'}: {'Two': 'N', 'Three': 'N', 'Four': 'N', 'Five': 'N', 'Six': 'N', 'Seven': 'N', 'Eight': 'N',
                       'Nine': 'N',
                       'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
    {'Queen', 'Queen'}: {'Two': 'N', 'Three': 'N', 'Four': 'N', 'Five': 'N', 'Six': 'N', 'Seven': 'N', 'Eight': 'N',
                         'Nine': 'N',
                         'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
    {'Jack', 'Jack'}: {'Two': 'N', 'Three': 'N', 'Four': 'N', 'Five': 'N', 'Six': 'N', 'Seven': 'N', 'Eight': 'N',
                       'Nine': 'N',
                       'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
    {'Ten', 'Ten'}: {'Two': 'N', 'Three': 'N', 'Four': 'N', 'Five': 'N', 'Six': 'N', 'Seven': 'N', 'Eight': 'N',
                     'Nine': 'N',
                     'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
    {'Nine', 'Nine'}: {'Two': 'Y', 'Three': 'Y', 'Four': 'Y', 'Five': 'Y', 'Six': 'Y', 'Seven': 'N', 'Eight': 'Y',
                       'Nine': 'Y',
                       'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
    {'Eight', 'Eight'}: {'Two': 'Y', 'Three': 'Y', 'Four': 'Y', 'Five': 'Y', 'Six': 'Y', 'Seven': 'Y', 'Eight': 'Y',
                         'Nine': 'Y',
                         'Ten': 'Y', 'Jack': 'Y', 'Queen': 'Y', 'King': 'Y', 'Ace': 'Y'},
    {'Seven', 'Seven'}: {'Two': 'Y', 'Three': 'Y', 'Four': 'Y', 'Five': 'Y', 'Six': 'Y', 'Seven': 'Y', 'Eight': 'N',
                         'Nine': 'N',
                         'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
    {'Six', 'Six'}: {'Two': 'N', 'Three': 'Y', 'Four': 'Y', 'Five': 'Y', 'Six': 'Y', 'Seven': 'N', 'Eight': 'N',
                     'Nine': 'N',
                     'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
    {'Five', 'Five'}: {'Two': 'N', 'Three': 'N', 'Four': 'N', 'Five': 'N', 'Six': 'N', 'Seven': 'N', 'Eight': 'N',
                       'Nine': 'N',
                       'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
    {'Four', 'Four'}: {'Two': 'N', 'Three': 'N', 'Four': 'N', 'Five': 'N', 'Six': 'N', 'Seven': 'N', 'Eight': 'N',
                       'Nine': 'N',
                       'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
    {'Three', 'Three'}: {'Two': 'N', 'Three': 'N', 'Four': 'Y', 'Five': 'Y', 'Six': 'Y', 'Seven': 'Y', 'Eight': 'N',
                         'Nine': 'N',
                         'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
    {'Two', 'Two'}: {'Two': 'N', 'Three': 'N', 'Four': 'Y', 'Five': 'Y', 'Six': 'Y', 'Seven': 'Y', 'Eight': 'N',
                     'Nine': 'N',
                     'Ten': 'N', 'Jack': 'N', 'Queen': 'N', 'King': 'N', 'Ace': 'N'},
}

# Initialize the deck and shuffle it
deck = Deck()
deck.shuffle()

# Initialize the player and dealer
player = Player("Player")
dealer = Player("Dealer")

# Main game loop
for i in range(int(input("number for shoe games : "))):
    # Deal the initial cards
    for _ in range(2):
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

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

# Define the card ranks, suits, and values
from Card import Card
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


# Define a class for the Deck
class Deck:
    def __init__(self):
        self.count = 0
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)
        self.count = 0

    def deal_card(self):
        self.count += 1
        return self.cards.pop()

# Define the card ranks, suits, and values
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


# Define a class for a Card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[ranks.index(rank)]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

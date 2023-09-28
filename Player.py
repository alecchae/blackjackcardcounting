# Define a class for the Player
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        if self.name == "Dealer":
            self.hiddenHand = []

    def add_card(self, card):
        if len(self.hand) > 0 and self.name == "Dealer":
            self.hiddenHand.append(card)
        else:
            self.hand.append(card)

    def calculate_score(self):
        score = sum(card.value for card in self.hand)
        # Handle aces
        for card in self.hand:
            if card.rank == 'Ace' and score > 21:
                score -= 10
        return score

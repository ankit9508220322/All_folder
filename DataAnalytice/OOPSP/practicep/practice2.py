import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{}->{}".format(self.suit, self.value)


class Deck:
    def __init__(self):
        suits = ['heart', 'diamond', 'clubs', 'spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
    
    def shuffle(self):
        if len(self.cards) < 52:
            print("Only full deck can be shuffled!")
        else:
            random.shuffle(self.cards)
        return self.cards

    def deal_card(self):
        if len(self.cards) == 0:
            print("All cards have been dealt!")
            return None
        return self.cards.pop()


deck = Deck()
print("Shuffled Deck:")
print(deck.shuffle())

print("\nOne Card Dealt:")
print(deck.deal_card())

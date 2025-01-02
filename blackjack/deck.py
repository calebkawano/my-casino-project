import random
from blackjack.card import Card

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
            '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 
            'King': 10, 'Ace': 11
        }
        self.cards = [Card(suit, rank, value) for suit in suits for rank, value in ranks.items()]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

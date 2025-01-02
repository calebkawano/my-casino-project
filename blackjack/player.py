class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)
        self.update_score()

    def update_score(self):
        self.score = sum(card.value for card in self.hand)
        # Handle Ace value adjustment
        aces = sum(1 for card in self.hand if card.rank == 'Ace')
        while self.score > 21 and aces:
            self.score -= 10
            aces -= 1

    def show_hand(self, hide_first_card=False):
        if hide_first_card:
            return f"[Hidden Card], " + ", ".join(str(card) for card in self.hand[1:])
        return ", ".join(str(card) for card in self.hand)

    def reset_hand(self):
        self.hand = []
        self.score = 0

from casino import Casino
from blackjack.deck import Deck
from blackjack.player import Player


class Blackjack(Casino):
    def __init__(self, game_number=Casino.DEFAULT_GAME_NUM, date=None, accountant=None):
        # Initialize the Casino parent class
        super().__init__(game_number, date, accountant)

        # Game-specific attributes
        self.deck = Deck()
        self.dealer = Player("Dealer")
        self.players = []

    def add_player(self, player_name):
        """Adds a new player to the blackjack game."""
        self.players.append(Player(player_name))

    def deal_initial_cards(self):
        """Deals initial cards to all players and the dealer."""
        for player in self.players:
            player.add_card(self.deck.deal())
            player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

    def play_round(self):
        """Plays a single round of Blackjack."""
        print("Starting Blackjack round!")

        # Deal initial cards
        self.deal_initial_cards()

        # Player turns
        for player in self.players:
            self.player_turn(player)

        # Dealer's turn
        self.dealer_turn()

        # Check winners
        self.check_winner()

        # Reset the game for the next round
        self.reset_game()

    def player_turn(self, player):
        """Manages a player's turn."""
        while player.score < 21:
            print(f"{player.name}'s turn. Hand: {player.show_hand()}, Score: {player.score}")
            choice = input("Hit or Stand? ").lower()
            if choice == 'hit':
                player.add_card(self.deck.deal())
            else:
                break

    def dealer_turn(self):
        """Manages the dealer's turn."""
        while self.dealer.score < 17:
            self.dealer.add_card(self.deck.deal())

    def check_winner(self):
        """Determines the winner of the round."""
        print(f"Dealer's hand: {self.dealer.show_hand()}, Score: {self.dealer.score}")
        for player in self.players:
            if player.score > 21:
                print(f"{player.name} busts! Dealer wins.")
            elif self.dealer.score > 21 or player.score > self.dealer.score:
                print(f"{player.name} wins!")
            elif player.score == self.dealer.score:
                print(f"{player.name} ties with the dealer.")
            else:
                print(f"Dealer wins against {player.name}.")

    def reset_game(self):
        """Resets the game for the next round."""
        self.deck = Deck()
        self.dealer.reset_hand()
        for player in self.players:
            player.reset_hand()

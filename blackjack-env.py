import random

class BlackjackEnvironment:
    def __init__(self, num_players):
        self.num_players = num_players
        self.deck = self.generate_deck()
        self.players = [self.initialize_player() for _ in range(num_players)]
        self.dealer_hand = []
        self.reset_game()

    def generate_deck(self):
        # Create a standard deck of 52 cards
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def initialize_player(self):
        # Initialize a player with an empty hand
        return {'hand': []}

    def deal_card(self, player):
        card = self.deck.pop()
        player['hand'].append(card)

    def calculate_hand_value(self, hand):
        # Calculate the value of a hand in Blackjack
        value = 0
        num_aces = 0

        for card in hand:
            rank = card['rank']
            if rank == 'A':
                value += 11
                num_aces += 1
            elif rank in ['K', 'Q', 'J']:
                value += 10
            else:
                value += int(rank)

        # Adjust for aces
        while num_aces > 0 and value > 21:
            value -= 10
            num_aces -= 1

        return value

    def reset_game(self):
        # Reset the game state for a new round
        self.deck = self.generate_deck()
        self.players = [self.initialize_player() for _ in range(self.num_players)]
        self.dealer_hand = []
        self.deal_initial_cards()

    def deal_initial_cards(self):
        # Deal two initial cards to each player and the dealer
        for _ in range(2):
            for player in self.players:
                self.deal_card(player)
            self.deal_card(self.dealer_hand)

    def play_game(self):
        # Players take turns to play, including the dealer
        for player in self.players:
            while self.calculate_hand_value(player['hand']) < 16:
                self.deal_card(player)

        # Determine the outcome for each player
        dealer_value = self.calculate_hand_value(self.players[-1]['hand'])  # Dealer is the last player in the list
        results = []

        for player in self.players[:-1]:  # Exclude the dealer from the results
            player_value = self.calculate_hand_value(player['hand'])
            if player_value > 21:
                result = 'Bust'
            elif dealer_value > 21 or player_value > dealer_value:
                result = 'Win'
            elif player_value == dealer_value:
                result = 'Push'
            else:
                result = 'Lose'
            results.append(result)

        return results

    def display_hands(self):
        print("Dealer's Hand:", ', '.join([f"{card['rank']} of {card['suit']}" for card in self.dealer_hand]))
        for i, player in enumerate(self.players):
            hand_value = self.calculate_hand_value(player['hand'])
            print(f"Player {i + 1} Hand: {', '.join([f'{card['rank']} of {card['suit']}' for card in player['hand']])} (Value: {hand_value})")

if __name__ == "__main__":
    num_players = 4  # You can set the number of players here
    blackjack_env = BlackjackEnvironment(num_players)
    
    # Play a round of Blackjack
    blackjack_env.play_game()
    blackjack_env.display_hands()

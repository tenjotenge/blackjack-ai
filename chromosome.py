import random

# Define possible dealer upcards and hands (combined into one array)
# T is J/Q/K, A is Ace
possible_upcards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "A"]

# Ace hands are specified with A-# since Ace values can differ
# Pairs are specified with D-#
possible_hands = [
    "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
    "18", "19", "20", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9",
    "D-2", "D-3", "D-4", "D-5", "D-6", "D-7", "D-8", "D-9", "D-T", "D-A"
]

# Create a 10x34 chromosome table to represent decisions (initialize with random decisions)
# S is stay, H is hit, D is double down, and P is split which is only possible for pairs
chromosome = [[random.choice(["S", "H", "D", "P"]) for _ in range(34)] for _ in range(10)]

# Define a function to calculate the index for the strategy decision in the chromosome
def calculate_index(upcard, hand):
    # Map the dealer upcard and hand to indices in the chromosome
    upcard_index = possible_upcards.index(upcard)
    hand_index = possible_hands.index(hand)
    
    return upcard_index * 34 + hand_index

# Example usage:
upcard = "5"  # Example dealer's upcard
hand = "13"   # Example hand (e.g., 13)
decision_index = calculate_index(upcard, hand)
decision = chromosome[possible_upcards.index(upcard)][decision_index]
print(f"Decision for Upcard {upcard} and Hand {hand}: {decision}")

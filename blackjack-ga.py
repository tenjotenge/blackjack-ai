import random

# Constants
POSSIBLE_UPCARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "A"]
POSSIBLE_HANDS = [
    "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
    "18", "19", "20", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9",
    "D-2", "D-3", "D-4", "D-5", "D-6", "D-7", "D-8", "D-9", "D-T", "D-A"
]
DECISIONS = ["H", "S", "D", "P"]  # Hit, Stand, Double-Down, Split

# GA Parameters - tweak as necessary
POPULATION_SIZE = 100
NUM_GENERATIONS = 50
TOURNAMENT_SIZE = 5
MUTATION_RATE = 0.02

def initialize_population():
    return [[random.choice(DECISIONS) for _ in range(len(POSSIBLE_UPCARDS) * len(POSSIBLE_HANDS))] for _ in range(POPULATION_SIZE)]

def calculate_fitness(chromosome):
    num_hands = 100
    initial_bankroll = 1000  # Adjust this based on your needs
    bet_amount = 10  # Adjust this based on your betting strategy

    total_money = initial_bankroll

    for _ in range(num_hands):
        # Simulate a hand of Blackjack using the strategy represented by the chromosome
        # Update total_money based on the result of the hand (win/lose) and betting
        hand_result = simulate_blackjack(chromosome, bet_amount)

        # Update total_money based on hand result and betting
        total_money += hand_result - bet_amount

    return total_money

def tournament_selection(population):
    # Select the best individual from a random tournament
    tournament_candidates = random.sample(population, TOURNAMENT_SIZE)
    return max(tournament_candidates, key=calculate_fitness)

def crossover(parent1, parent2):
    # Perform crossover to create a child
    crossover_point = random.randint(0, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(chromosome):
    # Perform mutation by randomly changing some decisions in the chromosome
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = random.choice(DECISIONS)
    return chromosome

def genetic_algorithm():
    # Main genetic algorithm
    population = initialize_population()

    for generation in range(NUM_GENERATIONS):
        # Evaluate fitness of each individual in the population
        fitness_scores = [calculate_fitness(chromosome) for chromosome in population]

        # Select parents using tournament selection
        parents = [tournament_selection(population) for _ in range(2 * POPULATION_SIZE)]

        # Create new population through crossover and mutation
        new_population = []

        for _ in range(POPULATION_SIZE):
            parent1, parent2 = random.choice(parents), random.choice(parents)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

        # Optional: Print the best fitness in each generation
        best_fitness = max(fitness_scores)
        print(f"Generation {generation + 1}, Best Fitness: {best_fitness}")

    # Return the best chromosome after the specified number of generations
    best_chromosome = max(population, key=calculate_fitness)
    return best_chromosome

def simulate_blackjack(chromosome, bet_amount):
    # Define constants for card values
    CARD_VALUES = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10,
        "J": 10, "Q": 10, "K": 10, "A": 11
    }

    # Define possible dealer upcards and hands
    possible_upcards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "A"]
    possible_hands = [
        "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9",
        "D-2", "D-3", "D-4", "D-5", "D-6", "D-7", "D-8", "D-9", "D-T", "D-A"
    ]

    # Create a 10x34 chromosome table for decisions (initialize with random decisions)
    chromosome = [[random.choice(["S", "H", "D"]) for _ in range(34)] for _ in range(10)]

    # Simulate a Blackjack hand
    dealer_upcard = random.choice(possible_upcards)
    player_hand = random.choice(possible_hands)

    # Use the chromosome to make decisions based on the dealer upcard and player hand
    decision_index = calculate_index(dealer_upcard, player_hand)
    decision = chromosome[possible_upcards.index(dealer_upcard)][decision_index]

    # Determine the outcome of the hand based on the decision (for simplicity, assume win or lose)
    if decision == "H":  # Hit
        player_value = calculate_hand_value(player_hand, CARD_VALUES)
        if player_value > 21:
            return -bet_amount  # Player busts, lose the bet
        else:
            return bet_amount   # Player survives, win the bet
    elif decision == "S":  # Stand
        return 0  # No change in money, hand is resolved without a win or loss
    elif decision == "D":  # Double down
        return 2 * bet_amount  # Double the bet for a win or loss

# Function to calculate the value of a hand
def calculate_hand_value(hand, card_values):
    value = 0
    num_aces = 0

    for card in hand.split("-"):
        rank = card[0]
        if rank == "A":
            value += 11
            num_aces += 1
        else:
            value += card_values[rank]

    # Adjust for aces
    while num_aces > 0 and value > 21:
        value -= 10
        num_aces -= 1

    return value

def calculate_index(upcard, hand):
    possible_upcards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "A"]
    possible_hands = [
        "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9",
        "D-2", "D-3", "D-4", "D-5", "D-6", "D-7", "D-8", "D-9", "D-T", "D-A"
    ]

    if upcard not in possible_upcards or hand not in possible_hands:
        raise ValueError("Invalid upcard or hand")

    upcard_index = possible_upcards.index(upcard)
    hand_index = possible_hands.index(hand)

    return upcard_index * 34 + hand_index


if __name__ == "__main__":
    best_chromosome = genetic_algorithm()
    print("Best Chromosome:", best_chromosome)

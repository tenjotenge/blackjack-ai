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
    # Calculate fitness by playing N hands of Blackjack and measuring total money
    # For simplicity, let's assume a fixed number of hands and a simple win/lose scenario
    num_hands = 100
    total_money = 0

    for _ in range(num_hands):
        # Simulate a hand of Blackjack using the strategy represented by the chromosome
        # Update total_money based on the result of the hand (win/lose)
        # You should replace this with your own simulation logic
        pass  # Placeholder, remove this line when you implement your logic

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

if __name__ == "__main__":
    best_chromosome = genetic_algorithm()
    print("Best Chromosome:", best_chromosome)

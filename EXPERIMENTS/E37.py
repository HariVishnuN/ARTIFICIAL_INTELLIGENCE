import numpy as np

# Goal: Maximize f(x) = x^2 where x is an integer between 0 and 31 (5-bit representation)
POP_SIZE = 6
GENE_LENGTH = 5
GENERATIONS = 10
MUTATION_RATE = 0.1

# Initialize random population of binary vectors
population = np.random.randint(0, 2, (POP_SIZE, GENE_LENGTH))

def binary_to_decimal(chrom):
    return int("".join(str(b) for b in chrom), 2)

for gen in range(GENERATIONS):
    # Calculate fitness for each chromosome
    decimals = np.array([binary_to_decimal(chrom) for chrom in population])
    fitness = decimals ** 2
    
    # Selection (Roulette Wheel selection probabilities)
    prob = fitness / np.sum(fitness)
    selected_indices = np.random.choice(POP_SIZE, size=POP_SIZE, p=prob)
    population = population[selected_indices]
    
    # Crossover (Single-point crossover)
    for i in range(0, POP_SIZE, 2):
        if i+1 < POP_SIZE:
            cp = np.random.randint(1, GENE_LENGTH)
            population[i, cp:], population[i+1, cp:] = population[i+1, cp:].copy(), population[i, cp:].copy()
            
    # Mutation
    for chrom in population:
        if np.random.rand() < MUTATION_RATE:
            idx = np.random.randint(GENE_LENGTH)
            chrom[idx] = 1 - chrom[idx]

best_idx = np.argmax(fitness)
print(f"Optimized Maximum Value Found: x = {decimals[best_idx]}, f(x) = {fitness[best_idx]}")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import random
from .genetic import genetic 


class Cluster:
    def __init__(self, X: np.array, y: np.array, size_population: int = 200, goal: float = 0.7, iters: int = 200) -> None:
        self.X = X
        self.y = y
        self.size_population = size_population
        self.goal = goal
        self.iters = iters

        self.n_samples = self.X.shape[0]
        self.genom = list(np.unique(y))

        self.population = []
        self.fitness = []

    def fit(self) -> None:
        for _ in range(self.size_population):
            chromosome = self._create_random_chromosome()
            self.population.append(genetic(chromosome, self.X, self.genom))

        self.counter = 1

        while True:
            # Sort by fitness scores in descending order
            self.population = sorted(self.population, key=lambda chromosome: chromosome.fitness_scores, reverse=True)

            if self.counter >= self.iters or (self.goal <= self.population[0].fitness_scores <= 1):
                break

            new_generation = []

            # Retain top 10% of the population
            size_best_people = int((10 * self.size_population) / 100)
            new_generation.extend(self.population[:size_best_people])

            # Generate children for the next generation (90% of population)
            for _ in range(int((90 * self.size_population) / 100)):
                parent1 = random.choice(self.population[:50])
                parent2 = random.choice(self.population[:50])
                child = parent1.generate(parent2)  # Assuming 'generate' exists in the 'genetic' class
                new_generation.append(child)

            self.population = new_generation

            # Apply mutation to the new population
            for index in range(self.size_population):
                self.population[index] = genetic(self.population[index].mutation(), self.X)

            # Update fitness scores
            self.fitness.append(self.population[0].fitness_scores)
            self.counter += 1
            self.show()

    def _create_random_chromosome(self) -> dict:
        chromosome = {index: random.choice(self.genom) for index in range(self.n_samples)}
        return chromosome

    def show(self) -> None:
        print(f"Loop: {self.counter}")
        print(f"===== >> Best Chromosome: {self.population[0]} \tFitness: {self.population[0].fitness_scores}")

    def show_plot(self) -> None:
        plt.plot(self.fitness)
        plt.title("Fitness Over Generations")
        plt.xlabel("Generation")
        plt.ylabel("Fitness Score")
        plt.show()

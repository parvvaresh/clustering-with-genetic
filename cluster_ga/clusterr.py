import numpy as np
import pandas as pd
from sklearn import datasets
import random
from .genetic import genetic_iris 

class cluster:
  def __init__(self, x, y,  size_population = 50, goal = 0.9, repeat = 100):
    self.x = x
    self.genom = list(np.unique(y))
    self.size_population = size_population
    self.goal = goal
    self.repeat = repeat
    self.population = []

  def fit(self):
    for _ in range(self.size_population):
      chromosome = self._creat_random_chromosome()
      self.population.append(genetic_iris(chromosome, self.x))
    self.counter = 1

    while True :
      if  self.counter == self.repeat:
        break
      self.population =  sorted(self.population, key=lambda chromosome : chromosome.fitness_scores, reverse = True)


      if self.goal <= self.population[0].fitness_scores <= 1:
        break

      new_generation = list()

      size_best_people = int((10 * self.size_population) / 100)
      new_generation.extend(self.population[: size_best_people])

      for _ in range(int((90 * self.size_population) / 100)):
        parent1 = random.choice(self.population[:50])
        parent2  = random.choice(self.population[:50])
        child = parent1.genrate(parent2)
        new_generation.append(child)
      
      self.population = new_generation

      for index in range(self.size_population):
        self.population[index] = genetic_iris(self.population[index].mutation(), self.x)

      self.counter += 1
      self.show()

  def _creat_random_chromosome(self):
    chromosome = dict()
    for index in range(self.x.shape[0]):
      chromosome[index] = random.choice(self.genom)
    return chromosome

  def show(self):
    print(f"loop is  : {self.counter}")
    print(f"generation: {self.population[0]} \tFitness: {self.population[0].fitness_scores}")

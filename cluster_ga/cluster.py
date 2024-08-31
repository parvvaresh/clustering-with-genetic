import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import random
from .genetic import genetic 


class cluster:
  def __init__(self, x : np.array, y : np.array,  size_population : int, goal : float, iters  : int) -> None:
    self.x = x
    self.y = y
    self.n_samples = x.shape[0]
    self.genom = list(np.unique(y))
    self.size_population = size_population
    self.goal = goal
    self.iters = iters

    self.population = []
    self.fitness = []


  def fit(self) -> None:
    for _ in range(self.size_population):
      chromosome = self._CreatRandomChromosome()
      self.population.append(genetic(chromosome, self.x))


    self.counter = 1

    while True :
      if  self.counter == self.iters and (self.goal <= self.population[0].fitness_scores and  self.population[0].fitness_scores <= 1):
        break
  
      self.population =  sorted(self.population, key=lambda chromosome : chromosome.fitness_scores, reverse = True)
      new_generation = list()

      size_best_people = int((10 * self.size_population) / 100)
      new_generation.extend(self.population[ : size_best_people])

      for _ in range(int((90 * self.size_population) / 100)):
        parent1 = random.choice(self.population[ : 50])
        parent2  = random.choice(self.population[ : 50])
        child = parent1.genrate(parent2)
        new_generation.append(child)
      
      self.population = new_generation

      for index in range(self.size_population):
        self.population[index] = genetic(self.population[index].mutation(), self.x)


      self.fitness.append(self.population[0].fitness_scores)
      self.counter += 1
      self.show()

  def _CreatRandomChromosome(self) -> dict:
    chromosome = {index: random.choice(self.genom) for index in range(self.n_samples)}
    return chromosome

  def show(self) -> None:
    print(f"loop is  : {self.counter}")
    print(f"===== >> generation: {self.population[0]} \tFitness: {self.population[0].fitness_scores}")

  def show_plot(self) -> None:
    plt.plot(self.fitness)

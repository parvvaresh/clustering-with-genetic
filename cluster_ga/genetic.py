import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn import datasets
import random

class genetic(object):
  def __init__(self, chromosome, points = None):
    self.chromosome = chromosome
    self.points = points
    self.list_class = list(set(datasets.load_iris().target))

    self.fitness_scores = self._get_fitness()

  def _get_fitness(self):
    
    labels = np.array(list((self.chromosome.values())))
    unique_labels = np.unique(labels)
        
    if len(unique_labels) < 2:
      return -1
        
    fitness_scores = silhouette_score(self.points, labels)
    return fitness_scores


  def mutation(self):
    probabality = random.random()
    if probabality >= 0.95:
      self._change_labels_to_nearest_center()
      self._change_random_label()
      self._assign_nearest_cluster_label()
      return self.chromosome

    return self.chromosome

  def genrate(self, parent):
    new_generation = dict()
    for index in range(len(self.chromosome)):

      probabality = random.random()
      
      if probabality < 0.45:
        new_generation[index] =  self.chromosome[index]
        
      elif probabality < 0.90:
        new_generation[index] = parent.chromosome[index]
        
      else:
        new_generation[index] =  random.choice(self.list_class)
        
    return genetic(new_generation, self.points)


  def _change_labels_to_nearest_center(self):
    sample_cluster_labels = random.choice(self.list_class)
    labels_neares_cluster = self._find_labels_neares_cluster(sample_cluster_labels)
    
    number_of_sample_cluster_labels = list(self.chromosome.values()).count(sample_cluster_labels)
    
    counter = 1
    for index in range(len(self.chromosome)):
      if self.chromosome[index] == sample_cluster_labels:
        self.chromosome[index] = labels_neares_cluster
        counter += 1
      if counter == number_of_sample_cluster_labels // 3:
        break

  def _find_labels_neares_cluster(self, sample_cluster_labels):
    sample_cluster = {}
    _sample_cluster = []
    for index in range(len(self.chromosome)):
      if self.chromosome[index] == sample_cluster_labels:
        _sample_cluster.append(self.points[index])
    sample_cluster[sample_cluster_labels] = _sample_cluster

    clusters = {}
    for _label in self.list_class:
      cluster = []
      if sample_cluster_labels != _label:
        for index, label in self.chromosome.items():
          if label == _label:
            cluster.append(self.points[index])
        clusters[_label] = cluster

    center_sample = self._find_cneter_cluster(sample_cluster[sample_cluster_labels])

    centers = []
    for cluster in clusters:
      temp = self._find_cneter_cluster(clusters[cluster])
      centers.append(temp)

    distance = []
    for center in centers:
      _distance = self._calcute_distance(center, center_sample)
      distance.append(_distance)

    distance = np.argsort(distance)
    index_nearest_center = distance[0]
    
    labels_neareset_cluster = list(clusters)[index_nearest_center]
    return labels_neareset_cluster

  def _find_cneter_cluster(self, cluster):
    data = list(map(np.array, cluster))
    data = np.array(data)
    center = np.mean(data, axis=0)
    return center

  def _assign_nearest_cluster_label(self):
    sample_index = random.choice(list(self.chromosome.keys()))

    _distance = []
    for index in range(len(self.chromosome)):
      _distance.append(self._calcute_distance(self.points[index], self.points[sample_index]))
    _distance = np.argsort(_distance)
    index_nearest_point = _distance[1]
    self.chromosome[sample_index] = self.chromosome[index_nearest_point]


  def _calcute_distance(self, point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    distance = np.sqrt(np.sum((point1 - point2) ** 2))
    return distance


  def _change_random_label(self):

    sample_index = random.choice(list(self.chromosome.keys()))
    sample_labels = random.choice(self.list_class)

    while sample_labels == self.chromosome[sample_index]:
      sample_labels = random.choice(self.list_class)
    self.chromosome[sample_index] = sample_labels  
    

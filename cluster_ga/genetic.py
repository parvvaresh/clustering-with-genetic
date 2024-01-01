import numpy as np
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn import datasets
import random

class genetic_iris(object):
  def __init__(self, chromosome, points = None):
    self.chromosome = chromosome
    self.points = iris = datasets.load_iris().data
    self.list_class = list(set(datasets.load_iris().target))

    self.fitness_scores = self._get_fitness()

  def _get_fitness(self):
    labels = np.array(list((self.chromosome.values())))
    fitness_scores = silhouette_score(self.points, labels)
    return fitness_scores

  def mutation(self):
    self._change_random_label()
    self._assign_nearest_cluster_label()
    self._change_labels_to_nearest_center()

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


    return genetic_iris(new_generation)


  def _change_labels_to_nearest_center(self):
    sample_cluster_labels = random.choice(self.list_class)
    labels_neares_cluster = self._find_labels_neares_cluster(sample_cluster_labels)

    for index in range(len(self.chromosome)):
      if self.chromosome[index] == sample_cluster_labels:
        self.chromosome[index] = labels_neares_cluster

  def _find_labels_neares_cluster(self, sample_cluster_labels):
    sample_cluster = []
    for index in range(len(self.chromosome)):
      if self.chromosome[index] == sample_cluster_labels:
        sample_cluster.appendlabel

    clusters = []
    for _label in self.list_class:
      cluster = {}
      if sample_cluster_labels != _label:
        for point, label in self.chromosome.items():
          if label == _label:
            cluster[point] = _label
      clusters.append(cluster)

    center_sample = self._find_cneter_cluster(sample_cluster)

    centers = []
    for cluster in clusters:
      temp = self._find_cneter_cluster(cluster)
      centers.append(temp)

    distance = []
    for center in centers:
      _distance = self._calcute_distance(center, center_sample)
      distance.append(_distance)

    distance = np.argsort(distance)
    index_nearest_center = distance[0]
    neareset_cluster = clusters[index_nearest_center]
    labels_neareset_cluster = list(neareset_cluster.values())[0]
    return labels_neareset_cluster

  def _find_cneter_cluster(self, cluster):
    data = np.array(cluster.keys())
    center = np.mean(data, axis=0)
    return center

  def _assign_nearest_cluster_label(self):
    sample_point = random.choice(self.points)

    _distance = []
    for point in self.points:
      _distance.append(self._calcute_distance(point, sample_point))
    _distance = np.argsort(_distance)
    index_nearest_point = _distance[1]
    self.chromosome[sample_point] = self.chromosome[list(self.chromosome)[index_nearest_point]]


  def _calcute_distance(self, point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    distance = np.sqrt(np.sum((point1 - point2) ** 2))


  def _change_random_label(self):

    sample_point = random.choice(self.points)
    sample_labels = random.choice(self.list_class)

    while sample_labels == self.chromosome[sample_point]:
      sample_labels = random.choice(self.list_class)
    self.chromosome[sample_point] = sample_labels
    
    
    
    
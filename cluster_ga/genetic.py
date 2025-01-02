import numpy as np
import random
from sklearn.metrics import silhouette_score

class GeneticClustering:
    def __init__(self, chromosome: dict, points: np.array, list_class: list) -> None:
        self.chromosome = chromosome
        self.points = points
        self.list_class = list_class

    def get_fitness(self):
        labels = np.array(list(self.chromosome.values()))
        unique_labels = np.unique(labels)

        if len(unique_labels) < 2:
            return -1

        return silhouette_score(self.points, labels)

    def mutate(self):
        if random.random() >= 0.95:
            self._change_labels_to_nearest_center()
            self._change_random_label()
            self._assign_nearest_cluster_label()
        return self.chromosome

    def generate(self, parent):
        new_generation = {}
        for index in range(len(self.chromosome)):
            prob = random.random()

            if prob < 0.45:
                new_generation[index] = self.chromosome[index]
            elif prob < 0.90:
                new_generation[index] = parent.chromosome[index]
            else:
                new_generation[index] = random.choice(self.list_class)

        return GeneticClustering(new_generation, self.points, self.list_class)

    def _change_labels_to_nearest_center(self):
        sample_cluster_label = random.choice(self.list_class)
        nearest_cluster_label = self._find_nearest_cluster(sample_cluster_label)

        sample_cluster_indices = [index for index, label in self.chromosome.items() if label == sample_cluster_label]
        num_changes = len(sample_cluster_indices) // 3

        for idx in sample_cluster_indices[:num_changes]:
            self.chromosome[idx] = nearest_cluster_label

    def _find_nearest_cluster(self, sample_cluster_label):
        sample_points = self.points[list(self.chromosome.values()) == sample_cluster_label]
        sample_center = np.mean(sample_points, axis=0)

        # Get centers of all other clusters
        other_clusters = {label: [] for label in self.list_class if label != sample_cluster_label}
        for index, label in self.chromosome.items():
            if label != sample_cluster_label:
                other_clusters[label].append(self.points[index])

        cluster_centers = {label: np.mean(np.array(points), axis=0) for label, points in other_clusters.items()}
        
        distances = {label: np.linalg.norm(sample_center - center) for label, center in cluster_centers.items()}
        nearest_label = min(distances, key=distances.get)
        return nearest_label

    def _assign_nearest_cluster_label(self):
        sample_index = random.choice(list(self.chromosome.keys()))
        distances = np.linalg.norm(self.points - self.points[sample_index], axis=1)
        nearest_index = np.argsort(distances)[1]  # 1st closest point
        self.chromosome[sample_index] = self.chromosome[nearest_index]

    def _change_random_label(self):
        sample_index = random.choice(list(self.chromosome.keys()))
        new_label = random.choice(self.list_class)

        while new_label == self.chromosome[sample_index]:
            new_label = random.choice(self.list_class)

        self.chromosome[sample_index] = new_label

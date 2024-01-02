# Genetic Clustering Algorithm for Iris Dataset

This Python script implements a genetic clustering algorithm for the Iris dataset using the KMeans algorithm as a base. The goal is to evolve a population of cluster assignments to find a set that maximizes the silhouette score, indicating better clustering.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Parameters](#parameters)
- [Example](#example)
- [License](#license)

## Introduction

The code employs a genetic algorithm to evolve a population of cluster assignments for the Iris dataset. The genetic algorithm includes mutation and crossover operations to generate new clusters and improve the overall fitness score based on silhouette scores.

## Features

- Genetic clustering algorithm for the Iris dataset.
- Utilizes the KMeans algorithm for clustering.
- Implements mutation and crossover operations for evolving cluster assignments.
- Prints information about each generation and the best fitness score.

## Dependencies

- numpy
- pandas
- scikit-learn

Install the required dependencies using:

```bash
pip install numpy pandas scikit-learn
```

## Usage

1. Clone the repository:

```bash
git clone <repository_url>
cd <repository_directory>
```

2. Run the script:

```bash
python ai.ipynb
```

## Parameters

- `size_population`: Size of the population (default: 500).
- `goal`: Target fitness score (default: 0.8).
- `repeat`: Maximum number of generations (default: 250).

Adjust these parameters in the `model` instantiation for customization.

## Example

```python
from your_module import cluster

# Load Iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
x = np.array(iris_df[["petal length (cm)", "petal width (cm)"]])
y = iris.target

# Instantiate and fit the model
model = cluster(x = x, y = y, size_population = 500, goal = 0.8, repeat = 250)
model.fit()
```

## License

This project is licensed under the MIT License - see the [LICENSE](MIT) file for details.


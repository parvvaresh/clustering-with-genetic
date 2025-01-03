# Genetic Clustering Algorithm

This Python script implements a genetic algorithm for clustering data. The algorithm optimizes the cluster assignments of data points using a genetic approach, aiming to improve the silhouette score. The silhouette score is a measure of how well-defined the clusters are in the data.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Overview](#algorithm-overview)
  - [Genetic Class](#genetic-class)
  - [Cluster Class](#cluster-class)
- [Parameters](#parameters)
- [Results](#results)
- [License](#license)
- [Acknowledgments](#acknowledgments)



## Installation




```bash
pip install cluster_ga
```

## Usage



```python
from sklearn import datasets
import numpy as np
import pandas as pd
from cluster_ga.cluster import cluster

# this is a for test

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
x = np.array(iris_df[["petal length (cm)", "petal width (cm)"]])
y = iris.target

# Instantiate and fit the model
model = cluster(x, y, 500, 0.9,150) 
model.fit()


# show fitness plot
model.show_plot()

```

## Algorithm Overview

The genetic clustering algorithm consists of the following components:

### Genetic Class

Defines the genetic operations such as mutation, generation, and fitness calculation.

### Cluster Class

Manages the clustering process, including the initialization of populations, evolution, and convergence.



## Parameters

- `size_population`: Number of individuals in the population.
- `goal`: The desired fitness score to achieve.
- `repeat`: Number of generations to run the algorithm.
- `is_mutation`: Boolean flag to enable or disable mutation.

## Results

The script outputs the progress of the algorithm, including the generation number and the fitness score achieved. Additionally, a plot of the fitness scores over generations is displayed at the end of the execution.

![result](./assets/result.png)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- This implementation is inspired by genetic algorithms and clustering techniques.
- Special thanks to the scikit-learn library for providing the silhouette score metric.

# Genetic Clustering Algorithm

This Python script implements a genetic algorithm for clustering data. The algorithm optimizes the cluster assignments of data points using a genetic approach, aiming to improve the silhouette score. The silhouette score is a measure of how well-defined the clusters are in the data.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Algorithm Overview](#algorithm-overview)
  - [Genetic Class](#genetic-class)
  - [Cluster Class](#cluster-class)
  - [Main Script](#main-script)
- [Parameters](#parameters)
- [Results](#results)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

- Python 3
- Required libraries: numpy, pandas, scikit-learn, matplotlib

### Installation

1. **Clone the repository:**

```bash
https://github.com/parvvaresh/clustering-with-genetic
cd clustering-with-genetic
```

2. **Install the required dependencies:**

```bash
pip install -r requirements.txt
```

## Usage

Run the `genetic_clustering.py` script to execute the genetic clustering algorithm on the provided dataset. Make sure to update the script with your dataset or use the default Iris dataset.

```bash
python3 test_iris.py
```

## Algorithm Overview

The genetic clustering algorithm consists of the following components:

### Genetic Class

Defines the genetic operations such as mutation, generation, and fitness calculation.

### Cluster Class

Manages the clustering process, including the initialization of populations, evolution, and convergence.

### Main Script

Utilizes the genetic and clustering classes to run the algorithm on a given dataset.

## Parameters

- `size_population`: Number of individuals in the population.
- `goal`: The desired fitness score to achieve.
- `repeat`: Number of generations to run the algorithm.
- `is_mutation`: Boolean flag to enable or disable mutation.

## Results

The script outputs the progress of the algorithm, including the generation number and the fitness score achieved. Additionally, a plot of the fitness scores over generations is displayed at the end of the execution.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- This implementation is inspired by genetic algorithms and clustering techniques.
- Special thanks to the scikit-learn library for providing the silhouette score metric.

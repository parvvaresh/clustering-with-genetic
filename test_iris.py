from sklearn import datasets
import numpy as np
import pandas as pd
# update import from main model


# this is a for test

iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
x = np.array(iris_df[["petal length (cm)", "petal width (cm)"]])
y = iris.target

# Instantiate and fit the model
model = cluster(x = x, y = y, size_population = 500, goal = 0.8, repeat = 250, is_mutation = True)
model.fit()

# see labels and clusters
print(model.population[0].chromosome)

# show fitness plot
model.show_plot()

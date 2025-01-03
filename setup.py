from setuptools import setup, find_packages

setup(
    name="cluster_ga",  # Name of your package
    version="0.2",      # Version of your package
    author="Alireza Parvaresh",
    author_email="parvvaresh@gmail.com",
    description="This Python script implements a genetic algorithm for clustering data. The algorithm optimizes the cluster assignments of data points using a genetic approach, aiming to improve the silhouette score. The silhouette score is a measure of how well-defined the clusters are in the data.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # This is optional
    url="https://github.com/parvvaresh/clustering-with-genetic",  # Link to your package’s homepage
    packages=find_packages(),  # Automatically find and include packages in your directory
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Adjust Python version as needed
)

# Company Clustering Customers
## Introduction
### This Python script performs clustering on customer data obtained from a company. The goal is to identify similar clients to propose relevant products based on their features. The script implements four different clustering methods and compares their results. Additionally, it utilizes two heuristics to determine the optimal number of clusters.

## Libraries Used

**NumPy:** For numerical operations and array manipulation.

**Matplotlib:** For data visualization, including plotting the clustering results.

**scikit-learn:** For implementing clustering algorithms and metrics.

**SciPy:** For computing the Euclidean distance between data points.

## Data

The customer data is stored in a NumPy array format and loaded from the file exercise_3/data.npy. Each row represents a customer, and there are four features for each customer.

## Clustering Methods
**K-means Clustering:** A partitioning method that aims to divide the data into K clusters.

Hierarchical Clustering: A hierarchical method that builds a tree of clusters.

## Distance Metrics

**Euclidean Distance:** The default distance metric used in K-means clustering and hierarchical clustering with the Euclidean linkage.

**Manhattan Distance:** Used as an alternative metric for K-means clustering.

## Heuristics for Choosing Number of Clusters

**Elbow Method:** Determines the optimal number of clusters by identifying the "elbow point" in the distortion plot.

**Silhouette Score:** Evaluates the quality of clustering by measuring the compactness and separation of clusters.

## Workflow

**Data Loading:** Load the customer data from the provided file and standardize it.

**Clustering Methods and Metrics Definition:** Define the clustering methods, including K-means and hierarchical clustering, along with their associated distance metrics.

**Elbow Method:** Determine the optimal number of clusters for each method using the Elbow method and plot the distortion curves.

**Silhouette Score:** Evaluate the silhouette scores for different numbers of clusters and select the one with the highest score.

**Clustering:**** Perform clustering using the selected number of clusters and store the results.

**Visualization:** Plot the clustering results for each method, visualizing the clusters in a 2D space.

## Conclusion

The script enables the comparison of different clustering methods and heuristics for determining the optimal number of clusters. By examining the clustering results and considering the insights provided by each method, the company can make informed decisions about segmenting its customers and tailoring products or services accordingly.


# Application of unsupervised learning

## Description of dataset

This dataset is a collection of 134 customer reviews from the McDonald's Facebook page in Sri Lanka. The reviews are in English and provide insights into customer experiences and sentiments regarding services and products. The data can be used for sentiment analysis, natural language processing (NLP), and customer feedback trends. It is ideal for beginner-level models in text analysis or to conduct a basic study of customer satisfaction trends in the fast-food industry in Sri Lanka.


## General analysis

**Number of observations:** The dataset contains 134 rows, which corresponds to the number of customer reviews.

**Number of variables:** The dataset contains 5 columns, which includes:
    date: Timestamp of the review
    text: The actual review text
    user/id: SHA-256 hashed user ID for anonymity
    user/name: SHA-256 hashed username for privacy protection

**Data types:**
    date: Date
    text: Text
    user/id: SHA-256
    user/name: SHA-256


## Statistical properties:

**Descriptive statistics:** Since the dataset mostly contains categorical variables, calculating descriptive statistics like mean, median, standard deviation, minimum and maximum wouldn't be applicable here.

**Frequency tables:** You can create frequency tables to analyze the distribution of the data in the categorical columns. For instance, you could create a frequency table to see how many reviews were posted each month or day of the week. This could help identify patterns in customer behavior.


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


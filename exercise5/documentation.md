# Application of unsupervised learning

## Description of dataset

This dataset is a collection of 134 customer reviews from the McDonald's Facebook page in Sri Lanka. The reviews are in English and provide insights into customer experiences and sentiments regarding services and products. The data can be used for sentiment analysis, natural language processing (NLP), and customer feedback trends. It is ideal for beginner-level models in text analysis or to conduct a basic study of customer satisfaction trends in the fast-food industry in Sri Lanka.
Link of DataSet: https://www.kaggle.com/datasets/kanchana1990/sri-lanka-mcdonalds-fb-reviews-data?resource=download


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


## Application:

# Analyse of the distribution of cluster
**Observations:** The majority of clusters (50%) have a size of 1, indicating that many data points are isolated and not well-grouped.
There are a significant number of clusters (40%) with a size of 2, suggesting some degree of clustering but still a lack of strong cluster formation.
Only 10% of clusters have a size of 3 or 4, indicating that larger, well-populated clusters are relatively rare.

**Interpretation:** The clustering results suggest that the data may not be well-suited for clustering using the chosen algorithm or parameters. The high proportion of small clusters indicates that many data points are not effectively grouped, and the low proportion of large clusters suggests that the algorithm is struggling to identify distinct and cohesive groups.$

# Analyse of dimensionality
**Observations:** The data points are spread out across the plot, suggesting that there is a high degree of variation within the dataset.
There is some overlap between the clusters, indicating that the clusters are not well-separated.
There are a few clusters that are more tightly grouped than others, suggesting that these clusters may be more cohesive.

**Interpretation:** The clustering results suggest that the data may be well-suited for dimensionality reduction, as the two principal components capture a significant portion of the variance in the data. However, the clustering itself may not be optimal, as there is a significant overlap between the clusters.

# Analyse of Variance

**Observations:** The data points are spread out across the plot, suggesting that there is a high degree of variation within the dataset.
There is some overlap between the clusters, indicating that the clusters are not well-separated.
There are a few clusters that are more tightly grouped than others, suggesting that these clusters may be more cohesive.
Interpretation:

**Interpretation:** The clustering results suggest that the data may be well-suited for dimensionality reduction, as the two principal components capture a significant portion of the variance in the data. However, the clustering itself may not be optimal, as there is a significant overlap between the clusters.
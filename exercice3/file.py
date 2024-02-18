import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from scipy.spatial.distance import cdist

# Load data
data = np.load('./data.npy')

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Define clustering methods
methods = [
    ('K-means (Euclidean)', KMeans),
    ('K-means (Manhattan)', KMeans),
    ('Hierarchical (Euclidean)', AgglomerativeClustering),
    ('Hierarchical (Rescaled Euclidean)', AgglomerativeClustering)
]

# Define distance metrics for each method
metrics = ['euclidean', 'manhattan', 'euclidean', 'euclidean']

# Initialize results dictionary
results = {}

# Perform clustering for each method
for (method_name, method), metric in zip(methods, metrics):
    # Determine the number of clusters using the Elbow method
    if method_name.startswith('K-means'):
        distortions = []
        K_range = range(1, 11)
        for k in K_range:
            kmeans = method(n_clusters=k, random_state=42)
            kmeans.fit(data_scaled)
            distortions.append(sum(np.min(cdist(data_scaled, kmeans.cluster_centers_, 'euclidean'), axis=1)) / data_scaled.shape[0])
        
        # Plot the Elbow curve
        plt.plot(K_range, distortions, 'bx-')
        plt.xlabel('Number of Clusters')
        plt.ylabel('Distortion')
        plt.title('Elbow Method for {}'.format(method_name))
        plt.show()

    # Determine the number of clusters using silhouette score
    silhouette_scores = []
    K_range = range(2, 11)
    for k in K_range:
        if method_name.startswith('K-means'):
            kmeans = method(n_clusters=k, random_state=42)
            labels = kmeans.fit_predict(data_scaled)
        else:
            clustering = method(n_clusters=k)
            labels = clustering.fit_predict(data_scaled)
        silhouette_scores.append(silhouette_score(data_scaled, labels, metric=metric))

    # Plot the Silhouette scores
    plt.plot(K_range, silhouette_scores, 'bx-')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Silhouette Score')
    plt.title('Silhouette Score for {}'.format(method_name))
    plt.show()

    # Choose the number of clusters based on the highest silhouette score
    best_k = K_range[np.argmax(silhouette_scores)]

    # Perform clustering with the chosen number of clusters
    if method_name.startswith('K-means'):
        kmeans = method(n_clusters=best_k, random_state=42)
        labels = kmeans.fit_predict(data_scaled)
    else:
        clustering = method(n_clusters=best_k)
        labels = clustering.fit_predict(data_scaled)

    # Store results
    results[method_name] = {
        'labels': labels,
        'num_clusters': best_k
    }

# Plot the clustering results
plt.figure(figsize=(15, 10))
for i, (method_name, result) in enumerate(results.items(), 1):
    plt.subplot(2, 2, i)
    plt.scatter(data[:, 0], data[:, 1], c=result['labels'], cmap='viridis', alpha=0.7)
    plt.title(method_name)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
plt.tight_layout()
plt.show()

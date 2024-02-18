import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from scipy.stats import entropy

# Load the dataset
data = pd.read_csv("mcdonalds_sri_lanka_reviews.csv")

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Perform text vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['text'])

# Perform clustering using KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
data['cluster'] = kmeans.fit_predict(X)

# Visualize the distribution of clusters
plt.figure(figsize=(8, 5))
sns.countplot(x='cluster', data=data, palette='viridis')
plt.title('Distribution of Clusters')
plt.xlabel('Cluster')
plt.ylabel('Count')
plt.show()

# Perform dimensionality reduction using Truncated SVD
svd = TruncatedSVD(n_components=2, random_state=42)
X_svd = svd.fit_transform(X)

# Rename the dimensions
data['semantic_feature_1'] = X_svd[:, 0]
data['semantic_feature_2'] = X_svd[:, 1]

# Visualize the reduced data with cluster labels
plt.figure(figsize=(10, 6))
sns.scatterplot(x='semantic_feature_1', y='semantic_feature_2', hue='cluster', data=data, palette='viridis', legend='full')
plt.title('Semantic Feature Representation with Cluster Labels')
plt.xlabel('Semantic Feature 1')
plt.ylabel('Semantic Feature 2')
plt.show()

# Calculate explained variance ratio
explained_variance_ratio = svd.explained_variance_ratio_

# Plot explained variance ratio
plt.figure(figsize=(8, 5))
plt.bar(range(len(explained_variance_ratio)), explained_variance_ratio, color='skyblue')
plt.title('Explained Variance Ratio')
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.show()

# Evaluate clustering using inertia
inertia = kmeans.inertia_
print("Inertia:", inertia)

# Evaluate dimensionality reduction using explained variance
print("Explained Variance Ratio:", explained_variance_ratio)

# Perform density estimation and calculate Kullback-Leibler divergence
# Calculate cluster proportions
cluster_proportions = data['cluster'].value_counts(normalize=True).sort_index().values

# Generate sampled distribution
sampled_distribution = np.random.dirichlet(alpha=np.ones(len(cluster_proportions)), size=len(data)).T

# Ensure the shapes are compatible for broadcasting
cluster_proportions = cluster_proportions.reshape(-1, 1)

# Calculate Kullback-Leibler divergence
kl_divergence = entropy(cluster_proportions, sampled_distribution)

print("Kullback-Leibler Divergence:", kl_divergence)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Load data and labels
data = np.load('./data.npy')
labels = np.load('./labels.npy')

# Perform PCA for dimensionality reduction to 2 dimensions
pca_2d = PCA(n_components=2)
data_pca_2d = pca_2d.fit_transform(data)

# Perform PCA for dimensionality reduction to 3 dimensions
pca_3d = PCA(n_components=3)
data_pca_3d = pca_3d.fit_transform(data)

# Perform t-SNE for dimensionality reduction to 2 dimensions
tsne_2d = TSNE(n_components=2)
data_tsne_2d = tsne_2d.fit_transform(data)

# Perform t-SNE for dimensionality reduction to 3 dimensions
tsne_3d = TSNE(n_components=3)
data_tsne_3d = tsne_3d.fit_transform(data)

# Plot PCA 2D
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(data_pca_2d[:, 0], data_pca_2d[:, 1], c=labels, cmap='coolwarm', alpha=0.7)
plt.title('PCA 2D')
plt.xlabel('PC1')
plt.ylabel('PC2')

# Plot PCA 3D
ax = plt.subplot(1, 2, 2, projection='3d')
ax.scatter(data_pca_3d[:, 0], data_pca_3d[:, 1], data_pca_3d[:, 2], c=labels, cmap='coolwarm', alpha=0.7)
ax.set_title('PCA 3D')
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')

plt.show()

# Plot t-SNE 2D
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(data_tsne_2d[:, 0], data_tsne_2d[:, 1], c=labels, cmap='coolwarm', alpha=0.7)
plt.title('t-SNE 2D')
plt.xlabel('Component 1')
plt.ylabel('Component 2')

# Plot t-SNE 3D
ax = plt.subplot(1, 2, 2, projection='3d')
ax.scatter(data_tsne_3d[:, 0], data_tsne_3d[:, 1], data_tsne_3d[:, 2], c=labels, cmap='coolwarm', alpha=0.7)
ax.set_title('t-SNE 3D')
ax.set_xlabel('Component 1')
ax.set_ylabel('Component 2')
ax.set_zlabel('Component 3')

plt.show()

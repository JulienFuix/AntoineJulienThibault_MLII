# 1. Sample n points from the joint distribution of X and Y:
import numpy as np
import matplotlib.pyplot as plt

# Parameters
mu_x, sigma_x = 1.7, 0.1
mu_y, sigma_y = 70, 10
n = 100  # number of samples

# Sample from the joint distribution
X = np.random.normal(mu_x, sigma_x, n)
Y = np.random.normal(mu_y, sigma_y, n)

# Plot the samples
plt.scatter(X, Y)
plt.xlabel('Height (m)')
plt.ylabel('Weight (kg)')
plt.title('Sampled Data Points')
plt.grid(True)
plt.show()
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

# Compute empirical average for increasing n
empirical_means = []
expected_value = np.array([mu_x, mu_y])

for i in range(1, n+1):
    empirical_mean = np.array([np.mean(X[:i]), np.mean(Y[:i])])
    empirical_means.append(empirical_mean)

# Compute euclidean distance between empirical average and expected value
distances = [np.linalg.norm(empirical_mean - expected_value) for empirical_mean in empirical_means]

# Plot the convergence
plt.plot(range(1, n+1), distances)
plt.xlabel('Number of Samples (n)')
plt.ylabel('Euclidean Distance')
plt.title('Convergence of Empirical Average to Expected Value')
plt.grid(True)
plt.show()

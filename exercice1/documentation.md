# Exercise 1: Data Distribution and the Law of Large Numbers
## Objective:
### The goal of this exercise is to manipulate a data distribution and become familiar with the Law of Large Numbers in an informal way.

# Implementation:
## Defining a 2-Dimensional Random Variable:

We propose a 2-dimensional random variable Z = (X, Y), where X represents the height of individuals in a population and Y represents their weight.

The joint distribution is defined as X ~ Normal(mu_x, sigma_x^2) and Y ~ Normal(mu_y, sigma_y^2), where mu_x, sigma_x, mu_y, and sigma_y are chosen parameters representing average height, standard deviation of height, average weight, and standard deviation of weight respectively.

## Sampling and Plotting:

We sample a number of points (n) from the joint distribution of X and Y.

Scatter plot is created to visualize the sampled data points.
Empirical Average and Convergence:

For increasing values of n, we compute the empirical average of the first n samples.

Euclidean distance between the empirical average and the expected value is plotted as a function of n to verify convergence to the expected value.

## Conclusion:

Through this exercise, we demonstrate how the Law of Large Numbers manifests in a simple scenario of sampling from a joint distribution and observing the convergence of empirical average to the expected value.


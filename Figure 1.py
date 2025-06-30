import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mu = 100       # Mean
sigma = 15     # Standard deviation

# Generate x values from μ - 4σ to μ + 4σ
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, color='skyblue', label='IQ Distribution')
plt.fill_between(x, y, color='skyblue', alpha=0.3)

# Set x-axis ticks in 15-point increments
tick_values = np.arange(mu - 3*sigma, mu + 3*sigma + 1, 15)
plt.xticks(tick_values)

# Axis labels only (no title, no value labels above the curve)
plt.xlabel('IQ Score')
plt.ylabel('Probability Density')

# Set y-axis to start from 0 to remove bottom gap
plt.ylim(bottom=0)

plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()

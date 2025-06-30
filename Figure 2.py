import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mu = 1430     # Mean SAT score
sigma = 30    # Standard deviation

# Generate x values from μ - 4σ to μ + 4σ
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, color='skyblue', label='SAT Score Distribution')
plt.fill_between(x, y, color='skyblue', alpha=0.3)

# Set x-axis ticks in 30-point increments
tick_values = np.arange(mu - 3*sigma, mu + 3*sigma + 1, 30)
plt.xticks(tick_values)

# Axis labels only
plt.xlabel('SAT Score Outcome Distribution (140 IQ)')
plt.ylabel('Probability Density')

# Set y-axis to start from 0 to remove bottom gap
plt.ylim(bottom=0)

plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()

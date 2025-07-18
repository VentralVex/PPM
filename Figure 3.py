import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define SAT score range (including values >1600 for modeling purposes)
x = np.linspace(1000, 1700, 1000)

# Initialize combined outcome distribution
y_total = np.zeros_like(x)

# Store means for simple average calculation
means = []

# Loop over IQ values from 140 to 160
for iq in range(140, 161):
    if iq <= 150:
        mu = 1430 + 17 * (iq - 140)
        sigma = 30
    else:
        mu = 1600
        sigma = 30 - 1.5 * (iq - 150)

    means.append(mu)  # Store for simple average

    # Create the SAT outcome distribution for this IQ
    y = norm.pdf(x, mu, sigma)
    y_total += y

# Average the distribution
y_avg = y_total / (160 - 140 + 1)

# -------- PLOTTING --------
plt.figure(figsize=(10, 5))
plt.plot(x, y_avg, color='purple', label='Aggregate SAT Outcome Distribution (IQ 140–160)')
plt.fill_between(x, y_avg, color='purple', alpha=0.3)

# Customize x-axis: ticks only up to 1600
tick_values = np.arange(1000, 1610, 100)
tick_labels = [str(tick) if tick < 1600 else '1600 →' for tick in tick_values]
plt.xticks(tick_values, tick_labels)

# Labels and layout
plt.xlabel('SAT Score')
plt.ylabel('Probability Density')
plt.title('Outcome Distribution for IQ 140–160')
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.xlim(1000, 1700)
plt.tight_layout()
plt.savefig('Figure 3.png')

# -------- EXPECTED VALUES --------

# Simple average of means (human obtainable approximation)
expected_simple = sum(means) / len(means)
print(f"Expected SAT score (simple average of means): {expected_simple:.2f}")

# True expected value from full outcome distribution
area = np.trapz(y_avg, x)
y_normalized = y_avg / area
expected_mixture = np.trapz(x * y_normalized, x)
print(f"Expected SAT score (mixture-based): {expected_mixture:.2f}")

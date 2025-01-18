import numpy as np
import matplotlib.pyplot as plt

# Generate multiple random walks
n_steps = 100
n_walks = 5

# Create the walks
walks = np.cumsum(np.random.normal(0, 1, (n_walks, n_steps)), axis=1)

# Calculate variances at each time point
variances = np.var(walks, axis=0)

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot random walks
for walk in walks:
    ax1.plot(walk, alpha=0.7)
ax1.set_title('Multiple Random Walks')
ax1.set_xlabel('Time')
ax1.set_ylabel('Value')

# Plot variances
ax2.plot(variances, color='red')
ax2.set_title('Variance Across Time')
ax2.set_xlabel('Time')
ax2.set_ylabel('Variance')

plt.tight_layout()
plt.show()
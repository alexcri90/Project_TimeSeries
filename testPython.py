import numpy as np

# Generate MA(2) process
n = 1000
epsilon = np.random.normal(0, 1, n+2)
y = epsilon[2:] + 0.6*epsilon[1:-1] + 0.3*epsilon[:-2]

# Theoretical ACF values for first few lags
acf_theoretical = np.zeros(4)
acf_theoretical[0] = 1  # lag 0
acf_theoretical[1] = (0.6 + 0.6*0.3)/(1 + 0.6**2 + 0.3**2)  # lag 1
acf_theoretical[2] = 0.3/(1 + 0.6**2 + 0.3**2)  # lag 2
acf_theoretical[3] = 0  # lag 3

# Sample ACF values for first few lags
acf_sample = np.zeros(4)
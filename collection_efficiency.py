import scipy.integrate as integrate
import numpy as np

# Define constants
E_gap = 1.1  # eV, bandgap energy for Silicon
k_B = 8.617e-5  # eV/K, Boltzmann constant
T = 6000  # K, temperature of the blackbody source

# x_gap = (E_gap)/(k_B.T)
# for Si, x_gap = (1.124 eV)/(8.617*10^-5 eV/K).(6000 K) = 2.1739

# Calculate x_gap
x_gap = E_gap / (k_B * T)

# Define the integrand for the numerator: x^2 / (e^x - 1)
def numerator_integrand(x):
    return x**2 / (np.exp(x) - 1)

# Define the integrand for the denominator: x^3 / (e^x - 1)
def denominator_integrand(x):
    return x**3 / (np.exp(x) - 1)

# Compute the numerator integral from x_gap to ∞
numerator, _ = integrate.quad(numerator_integrand, x_gap, np.inf)

# Compute the denominator integral from 0 to ∞
denominator, _ = integrate.quad(denominator_integrand, 0, np.inf)

# Compute the maximum collection efficiency
eta_collection_max = x_gap * (numerator / denominator)

# Display the result
print("Maximum Collection Efficiency (η_collection^max):", eta_collection_max)

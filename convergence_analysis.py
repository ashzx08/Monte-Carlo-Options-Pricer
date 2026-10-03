import numpy as np
import matplotlib.pyplot as plt

number_of_simulations = np.array([10000, 25000, 50000, 100000, 250000, 500000, 1000000])
monte_carlo_prices = np.array([5.84, 5.76, 5.76, 5.80, 5.77, 5.75, 5.76])
standard_errors = np.array([0.08, 0.05, 0.03, 0.02, 0.02, 0.01, 0.01])
absolute_errors = np.array([0.07401, 0.00580, 0.00257, 0.03381, 0.01201, 0.01724, 0.00155])
black_scholes_price = 5.76

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
ax1.plot(number_of_simulations, monte_carlo_prices, marker="o", label="Monte Carlo Price")
ax1.axhline(black_scholes_price, linestyle="--", color="red", label="Black-Scholes Price")
ax1.set_xscale("log")
ax1.set_xlabel("Number of Simulations")
ax1.set_ylabel("Option Price (£)")
ax1.set_title("Monte Carlo Option Price Convergence")
ax1.legend()
ax1.grid(True, which="both", linestyle=":", alpha=0.6)

ax2.plot(number_of_simulations, standard_errors, marker="o", color="orange")
ax2.set_xscale("log")
ax2.set_xlabel("Number of Simulations")
ax2.set_ylabel("Standard Error (£)")
ax2.set_title("Monte Carlo Standard Error")
ax2.grid(True, which="both", linestyle=":", alpha=0.6)

ax3.plot(number_of_simulations, absolute_errors, marker="o", color="red")
ax3.set_xscale("log")
ax3.set_xlabel("Number of Simulations")
ax3.set_ylabel("Absolute Error (£)")
ax3.set_title("Monte Carlo Absolute Error")
ax3.grid(True, which="both", linestyle=":", alpha=0.6)

plt.tight_layout()
plt.savefig("convergence_analysis.png", dpi=300, bbox_inches="tight")
plt.show()
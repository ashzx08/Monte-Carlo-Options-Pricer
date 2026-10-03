import numpy as np
import matplotlib.pyplot as plt

from monte_carlo import MonteCarloPricer
from StockSimulation import StockSimulator
from option import EuropeanCall
from BlackScholes import BlackScholes


stock_price = 100
strike_price = 100
time_to_expiration = 0.5
risk_free_rate = 0.05
number_of_steps = 126
number_of_simulations = 100000

volatilities = np.array([0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40])

monte_carlo_prices = []
black_scholes_prices = []


for volatility in volatilities:

    stock = StockSimulator(stock_price, time_to_expiration, risk_free_rate, volatility, number_of_steps)
    option = EuropeanCall(strike_price)
    pricer = MonteCarloPricer(stock, option, number_of_simulations)

    monte_carlo_price, _, _, _ = pricer.option_price()

    black_scholes = BlackScholes(stock_price, strike_price, time_to_expiration, risk_free_rate, volatility)

    monte_carlo_prices.append(monte_carlo_price)
    black_scholes_prices.append(black_scholes.call_price())


monte_carlo_prices = np.array(monte_carlo_prices)
black_scholes_prices = np.array(black_scholes_prices)


plt.figure(figsize=(10, 6))

plt.plot(volatilities, monte_carlo_prices, marker="o", label="Monte Carlo Price")

plt.plot(volatilities, black_scholes_prices, marker="o", linestyle="--", label="Black-Scholes Price")

plt.xlabel("Annual Volatility")
plt.ylabel("Option Price (£)")
plt.title("Option Price Sensitivity to Volatility")

plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)

plt.tight_layout()
plt.savefig("volatility_sensitivity.png", dpi=300, bbox_inches="tight")
plt.show()
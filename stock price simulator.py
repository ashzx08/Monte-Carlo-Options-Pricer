import numpy as np
import matplotlib.pyplot as plt

Initial_stock_price = 100
current_price = Initial_stock_price
final_stock_prices = []
option_payoffs = []
Number_of_steps = 252
Number_of_simulations = 10000
r = 0.05
annual_volatility = 0.01*np.sqrt(252)
delta_t = 1/Number_of_steps
T = 1

def option_payoff_calculation(final_stock_price, strike_price):
    payoff = max(final_stock_price - strike_price, 0)
    return payoff

def stock_price_calculation(stock_price, v=annual_volatility, dt=delta_t, r=r):
    Z = np.random.normal(loc=0, scale=1)
    drift = (r - 0.5*(v**2))*dt
    diffusion = v*np.sqrt(dt)*Z
    new_price = stock_price*np.exp(drift + diffusion)
    return new_price

def simulate_year(Initial_stock_price):
    current_stock_price = Initial_stock_price
    for _ in range(Number_of_steps):
        new_price = stock_price_calculation(current_stock_price)
        current_stock_price = new_price
    return current_stock_price

for _ in range(Number_of_simulations):
    final_price = simulate_year(Initial_stock_price)
    payoff = option_payoff_calculation(final_price, Initial_stock_price)
    option_payoffs.append(payoff)
    final_stock_prices.append(final_price)

numpy_option_payoffs = np.array(option_payoffs)
numpy_final_prices = np.array(final_stock_prices)
option_value = (np.exp(-r*T))*np.mean(numpy_option_payoffs)
standard_error = (np.exp(-r*T))*np.std(numpy_option_payoffs) / np.sqrt(Number_of_simulations)

print(f"Number of simulations: {Number_of_simulations}")
print(f"Standard error of the option value estimate: £{standard_error:.2f}")
print(f"Estimated option value: £{option_value:.2f}")
print(f"Average final stock price: £{np.mean(numpy_final_prices):.2f}")

plt.hist(numpy_option_payoffs)
plt.title("Histogram of Option Payoffs in Stock Price Simulation")
plt.show()
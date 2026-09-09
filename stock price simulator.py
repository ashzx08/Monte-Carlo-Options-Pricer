import numpy as np
import matplotlib.pyplot as plt

Initial_stock_price = 100
current_price = Initial_stock_price
final_stock_prices = []
option_payoffs = []
Number_of_steps = 252
Number_of_simulations = 10000
r = 0.05
T = 1

def option_payoff_calculation(final_stock_price, strike_price):
    payoff = max(final_stock_price - strike_price, 0)
    return payoff

def stock_price_calculation(stock_price):
    return_percentage = np.random.normal(loc=0, scale=0.01)
    new_price = stock_price * (1 + return_percentage)
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

print(f"Mean final stock price after one year: £{np.mean(numpy_final_prices):.2f}")
print(f"Mean option payoff after one year: £{np.mean(numpy_option_payoffs):.2f}")
print(f"Estimated option value: £{option_value:.2f}")

plt.hist(numpy_option_payoffs)
plt.title("Histogram of Option Payoffs in Stock Price Simulation")
plt.show()
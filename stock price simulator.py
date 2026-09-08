import numpy as np
import matplotlib.pyplot as plt

Initial_stock_price = 100
current_price = Initial_stock_price
final_stock_prices = []
Number_of_steps = 252
Number_of_simulations = 10000

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
    final_stock_prices.append(final_price)

numpy_final_prices = np.array(final_stock_prices)

print("Mean final stock price after one year: ", np.mean(numpy_final_prices))
print("Standard deviation of final stock prices: ", np.std(numpy_final_prices))
print("Minimum final stock price: ", np.min(numpy_final_prices))
print("Maximum final stock price: ", np.max(numpy_final_prices))

plt.hist(numpy_final_prices)
plt.title("Distribution of Final Stock Prices After One Year")
plt.show()
import numpy as np
import matplotlib.pyplot as plt

Initial_stock_price = 100
current_price = Initial_stock_price
stock_prices = [Initial_stock_price]
Number_of_steps = 252

def stock_price_calculation(stock_price):
    return_price = np.random.normal(loc=0, scale=0.01)
    new_price = stock_price * (1 + return_price)
    return new_price

for _ in range(Number_of_steps):
    new_price = stock_price_calculation(current_price)
    current_price = new_price
    stock_prices.append(new_price)

numpy_stock_prices = np.array(stock_prices)

print(f"Final stock price: {current_price}")
plt.plot(numpy_stock_prices)
plt.title("Stock Price Simulation Over Time")
plt.show()

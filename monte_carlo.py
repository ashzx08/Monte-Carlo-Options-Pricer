import numpy as np
from option import EuropeanCall
from StockSimulation import StockSimulator
import time

class MonteCarloPricer:

    def __init__(self, stock_simulator, option, number_of_simulations):
        self.stock_simulator = stock_simulator
        self.option = option
        self.N = number_of_simulations

    def simulate_payoffs(self):
        final_prices = self.stock_simulator.simulate_final_prices(self.N)
        option_payoffs = self.option.payoff(final_prices)
        return option_payoffs

    def option_price(self):
        option_payoffs = self.simulate_payoffs()
        average_payoff = np.mean(option_payoffs)
        discount_factor = np.exp(-(self.stock_simulator.r) * (self.stock_simulator.T))
        option_value = discount_factor * (average_payoff)
        standard_error = discount_factor * (np.std(option_payoffs) / np.sqrt(self.N))
        confidence_interval = (option_value - 1.96 * standard_error, option_value + 1.96 * standard_error)
        return option_value, option_payoffs, standard_error, confidence_interval
        

stock1 = StockSimulator(100, 0.5, 0.05, 0.1587, 126)
option1 = EuropeanCall(100)
stock_pricer1 = MonteCarloPricer(stock1, option1, 100000)


option_value, option_payoffs, standard_error, confidence_interval = stock_pricer1.option_price()

print(f"Option price: £{option_value:.2f}")
print(f"Standard error: £{standard_error:.2f}")
print(f"95% Confidence Interval: £{confidence_interval[0]:.2f} - £{confidence_interval[1]:.2f}")
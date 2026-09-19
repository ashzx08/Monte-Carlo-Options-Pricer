import numpy as np
from option import EuropeanCall
from StockSimulation import StockSimulator
import time

class MonteCarloPricer:

    def __init__(self, stock_simulator, option, number_of_simulations):
        self.stock_simulator = stock_simulator
        self.option = option
        self.N = number_of_simulations

    def Monte_Carlo_Simulations(self):
        final_prices = self.stock_simulator.simulate_final_prices(self.N)
        option_payoffs = self.option.payoff(final_prices)
        return option_payoffs

    def option_price(self):
        option_payoffs = self.Monte_Carlo_Simulations()
        average_payoff = np.mean(option_payoffs)
        option_value = np.exp(-(self.stock_simulator.r) * (self.stock_simulator.T)) * (average_payoff)
        return option_value, option_payoffs
        

stock1 = StockSimulator(100, 0.5, 0.05, 0.1587, 126)
option1 = EuropeanCall(100)
stock_pricer1 = MonteCarloPricer(stock1, option1, 100000)

start = time.perf_counter()

option_value, option_payoffs = stock_pricer1.option_price()

end = time.perf_counter()

print(option_payoffs.shape)
print(f"Option price: £{option_value:.2f}")
print(f"Time taken: {end - start:.4f} seconds")
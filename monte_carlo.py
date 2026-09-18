import numpy as np
from option import EuropeanCall
from StockSimulation import StockSimulator

class MonteCarloPricer:

    def __init__(self, stock_simulator, option, number_of_simulations):
        self.stock_simulator = stock_simulator
        self.option = option
        self.N = number_of_simulations

    def Monte_Carlo_Simulations(self):
        option_payoffs = []
        for _ in range(self.N):
            path = self.stock_simulator.simulate_path()
            final_price = path[-1]
            payoff = self.option.payoff(final_price)
            option_payoffs.append(payoff)

        return option_payoffs

    def option_price(self):
        option_payoffs = np.array(self.Monte_Carlo_Simulations())
        average_payoff = np.mean(option_payoffs)
        option_value = np.exp(-(self.stock_simulator.r) * (self.stock_simulator.T)) * (average_payoff)
        return option_value
        

stock1 = StockSimulator(100, 0.5, 0.05, 0.1587, 126)
option1 = EuropeanCall(100)
stock_pricer1 = MonteCarloPricer(stock1, option1, 10000)

option_value = stock_pricer1.option_price()
print(option_value)
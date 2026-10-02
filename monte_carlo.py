import numpy as np
from option import EuropeanCall
from StockSimulation import StockSimulator

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
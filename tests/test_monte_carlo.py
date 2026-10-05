import numpy as np

from monte_carlo import MonteCarloPricer
from StockSimulation import StockSimulator
from option import EuropeanCall

def test_monte_carlo_price_is_positive():
    simulator = StockSimulator(stock_price=100, time_to_expiration=0.5, risk_free_rate=0.05, annual_volatility=0.1587, number_of_steps=126)
    option = EuropeanCall(100)
    pricer = MonteCarloPricer(simulator, option, number_of_simulations=10000)

    option_value, _, _, _ = pricer.option_price()

    assert option_value > 0

def test_monte_carlo_returns_correct_number_of_payoffs():
    simulator = StockSimulator(stock_price=100, time_to_expiration=0.5, risk_free_rate=0.05, annual_volatility=0.1587, number_of_steps=126)
    option = EuropeanCall(100)
    pricer = MonteCarloPricer(simulator, option, number_of_simulations=10000)

    option_payoffs = pricer.simulate_payoffs()

    assert len(option_payoffs) == 10000

def test_monte_carlo_price_is_close_to_black_scholes():
    simulator = StockSimulator(stock_price=100, time_to_expiration=0.5, risk_free_rate=0.05, annual_volatility=0.1587, number_of_steps=126)
    option = EuropeanCall(100)
    pricer = MonteCarloPricer(simulator, option, number_of_simulations=100000)

    option_value, _, standard_error, confidence_interval = pricer.option_price()

    black_scholes_price = 5.76

    assert abs(option_value - black_scholes_price) < 3 * standard_error
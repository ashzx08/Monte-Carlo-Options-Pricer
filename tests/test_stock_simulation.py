import numpy as np

from StockSimulation import StockSimulator


def test_simulate_step_returns_positive_price():
    simulator = StockSimulator(stock_price=100, time_to_expiration=0.5, risk_free_rate=0.05, annual_volatility=0.1587, number_of_steps=126)
    new_price = simulator.simulate_step(100)

    assert new_price > 0

def test_simulate_path_has_correct_length():
    simulator = StockSimulator(stock_price=100, time_to_expiration=0.5, risk_free_rate=0.05, annual_volatility=0.1587, number_of_steps=126)
    path = simulator.simulate_path()

    assert len(path) == 127

def test_simulate_path_starts_at_initial_price():
    simulator = StockSimulator(stock_price=100, time_to_expiration=0.5, risk_free_rate=0.05, annual_volatility=0.1587, number_of_steps=126)
    path = simulator.simulate_path()

    assert path[0] == 100

def test_simulate_final_prices_are_positive():
    simulator = StockSimulator(stock_price=100, time_to_expiration=0.5, risk_free_rate=0.05, annual_volatility=0.1587, number_of_steps=126)
    final_prices = simulator.simulate_final_prices(1000)

    assert len(final_prices) == 1000
    assert np.all(final_prices > 0)
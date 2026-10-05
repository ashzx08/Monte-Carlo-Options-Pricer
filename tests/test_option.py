import numpy as np
from option import EuropeanCall

def test_call_below_strike():
    option = EuropeanCall(100)
    payoff = option.payoff(np.array([90]))

    assert payoff[0] == 0

def test_call_at_strike():
    option = EuropeanCall(100)
    payoff = option.payoff(np.array([100]))

    assert payoff[0] == 0

def test_call_above_strike():
    option = EuropeanCall(100)
    payoff = option.payoff(np.array([120]))

    assert payoff[0] == 20

def test_multiple_payoffs():
    option = EuropeanCall(100)
    final_prices = np.array([80, 100, 120, 150])
    payoffs = option.payoff(final_prices)

    expected_payoffs = np.array([0, 0, 20, 50])

    assert np.array_equal(payoffs, expected_payoffs)
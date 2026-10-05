from BlackScholes import BlackScholes


def test_black_scholes_call_price():
    option = BlackScholes(stock_price=100, strike_price=100, time_to_expiration=0.5, risk_free_rate=0.05, annual_volatility=0.1587)
    price = option.call_price()

    assert abs(price - 5.76) < 0.01

def test_black_scholes_call_price_increases_with_volatility():
    low_volatility = BlackScholes(100, 100, 0.5, 0.05, 0.10)
    high_volatility = BlackScholes(100, 100, 0.5, 0.05, 0.30)

    assert high_volatility.call_price() > low_volatility.call_price()
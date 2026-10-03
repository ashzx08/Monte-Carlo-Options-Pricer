from monte_carlo import MonteCarloPricer
from StockSimulation import StockSimulator
from option import EuropeanCall
from BlackScholes import BlackScholes

stock_price, strike_price, time_to_expiration, risk_free_rate, annual_volatility, number_of_steps, number_of_simulations = 100, 100, 0.5, 0.05, 0.1587, 126, 100000
stock1 = StockSimulator(stock_price, time_to_expiration, risk_free_rate, annual_volatility, number_of_steps)
option1 = EuropeanCall(strike_price)
stock_pricer1 = MonteCarloPricer(stock1, option1, number_of_simulations)
black_scholes = BlackScholes(stock_price, strike_price, time_to_expiration, risk_free_rate, annual_volatility)

option_value, option_payoffs, standard_error, confidence_interval = stock_pricer1.option_price()
difference = abs(option_value - black_scholes.call_price())

def stock_detail():
    print(f"Number of simulations: {number_of_simulations}")
    print(f"Initial stock price: {stock_price}")
    print(f"Strike Price: {strike_price}")
    print(f"Annual volatility: {annual_volatility}")
    print(f"Risk free rate: {risk_free_rate}\n")
    print(f"Option price: £{option_value:.2f}")
    print(f"Standard error: £{standard_error:.2f}")
    print(f"95% Confidence Interval: £{confidence_interval[0]:.2f} - £{confidence_interval[1]:.2f}")
    print(f"Black-Scholes price: £{black_scholes.call_price():.2f}")
    print(f"Absolute difference: £{difference:.5f}")

stock_detail()
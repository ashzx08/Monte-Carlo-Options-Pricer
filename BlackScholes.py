import numpy as np
import scipy.stats as sp

class BlackScholes:

    def __init__(self, stock_price, strike_price, time_to_expiration, risk_free_rate, annual_volatility):
        self.Stock_price = stock_price
        self.Strike_price = strike_price
        self.time_to_expiration = time_to_expiration
        self.risk_free_rate = risk_free_rate
        self.annual_volatility = annual_volatility

    def call_price(self):

        # Formula for black-scholes call option price
        # C = S * N(d1) - K * exp(-r * T) * N(d2)
        # where:
        # d1 = (ln(S/K) + (r + 0.5 * annual_volatility^2) * T) / (annual_volatility * sqrt(T))
        # d2 = d1 - annual_volatility * sqrt(T)

        d1 = (np.log(self.Stock_price/self.Strike_price) + (self.risk_free_rate + 0.5 * self.annual_volatility**2) * self.time_to_expiration) / (self.annual_volatility * np.sqrt(self.time_to_expiration))
        d2 = d1 - self.annual_volatility * np.sqrt(self.time_to_expiration)
        N_d1 = sp.norm.cdf(d1)
        N_d2 = sp.norm.cdf(d2)
        call_price = self.Stock_price * N_d1 - self.Strike_price * np.exp(-self.risk_free_rate * self.time_to_expiration) * N_d2
        return call_price
class EuropeanCall:

    def __init__(self, strike_price):
        self.strike_price = strike_price

    def payoff(self, final_price):
        return max((final_price - self.strike_price), 0)

import numpy as np

class StockSimulator:

    def __init__(self, stock_price, time_to_expiration, risk_free_rate, annual_volatility, number_of_steps):
        self.S = stock_price
        self.T = time_to_expiration
        self.r = risk_free_rate
        self.V_a=annual_volatility
        self.number_of_steps = number_of_steps
        self.delta_t = self.T / self.number_of_steps

    def simulate_step(self, current_price):

        # Simulate a single step in the stock price path using Geometric Brownian Motion
        # S(t+dt) = S(t) * exp(drift + diffusion)
        # drift = (risk_free_rate - 0.5 * volatility^2) * dt
        # diffusion = volatility * sqrt(dt) * Z
        # dt is the time increment
        # Z is a random variable drawn from a standard normal distribution

        Z = np.random.normal(loc=0, scale=1)

        # Calculate the drift and diffusion components of the stock price change
        drift = (self.r - 0.5 * (self.V_a **2)) * self.delta_t
        diffusion = self.V_a * np.sqrt(self.delta_t) * Z

        # Calculate the new stock price based on the current price, drift, and diffusion
        new_price = current_price * np.exp(drift + diffusion)
        return new_price

    def simulate_path(self):
        Z = np.random.normal(loc=0, scale=1, size=self.number_of_steps)
        
        # Calculate the drift and diffusion components of the stock price change
        drift = (self.r - 0.5 * (self.V_a **2)) * self.delta_t
        diffusion = self.V_a * np.sqrt(self.delta_t) * Z
        
        # Calculate the new stock prices based on the current price, drift, and diffusion
        step_multipliers = np.exp(drift + diffusion)
        cumulative_multipliers = np.cumprod(step_multipliers)
        stock_prices = np.insert(self.S * cumulative_multipliers, 0, self.S)
        return stock_prices

    def simulate_paths(self, number_of_simulations):
        Z = np.random.normal(loc=0, scale=1, size=((number_of_simulations, self.number_of_steps)))

        # Calculate the drift and diffusion components of the stock price change
        drift = (self.r - 0.5 * (self.V_a **2)) * self.delta_t
        diffusion = self.V_a * np.sqrt(self.delta_t) * Z

        # Calculate the new stock prices based on the current price, drift, and diffusion
        step_multipliers = np.exp(drift + diffusion)
        cumulative_multipliers = np.cumprod(step_multipliers, axis=1)

        # Creating a 2D array with the intial value being initial stock price and stacking the array of paths onto it
        initial_prices = np.full((number_of_simulations, 1), self.S)
        stock_prices = np.hstack((initial_prices, self.S*cumulative_multipliers))
        return stock_prices

    def simulate_final_prices(self, number_of_simulations):
        Z = np.random.normal(loc=0, scale=1, size=number_of_simulations)

        # Calculate the drift and diffusion components of the stock price change
        drift = (self.r - 0.5 * (self.V_a **2)) * self.T
        diffusion = self.V_a * np.sqrt(self.T) * Z

        return self.S * np.exp(drift + diffusion)
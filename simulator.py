import numpy as np

class MonteCarloSimulator:
    
    def __init__(self, returns_df, weights):
      
        self.returns_df = returns_df
        self.weights = weights
        
        # calculate trnasition matrix
        self.mean_returns = returns_df.mean().values
        self.cov_matrix = returns_df.cov().values
        
        self._print_statistics()
    
    def _print_statistics(self):
        print("Historical Statistics (Daily):")
        print(f"{'Symbol':<8} {'Mean Return':<15} {'Volatility'}")
        print("-" * 45)
        
        for i, symbol in enumerate(self.returns_df.columns):
            mean_pct = self.mean_returns[i] * 100
            std_pct = np.sqrt(self.cov_matrix[i,i]) * 100
            print(f"{symbol:<8} {mean_pct:>6.4f}%        {std_pct:>6.4f}%")
        
        print("\nTransition Matrix :")
        print(self.returns_df.corr().round(3))
        print()
    
    def run_simulation(self, n_simulations):
        
        print(f"   Running Monte Carlo Simulation...")
        print(f"   Number of simulations: {n_simulations:,}")
        
        # This is like the transition matrix P from the diamond graph
        # But for continuous return space instead of discrete nodes
        simulated_returns = np.random.multivariate_normal(
            self.mean_returns,    # Expected returns (like stationary distribution)
            self.cov_matrix,      # How assets covary (like transition probabilities)
            n_simulations         # Number of paths to simulate
        )
        
        # Calculate portfolio return for each simulation
        # @ is matrix multiplication: returns x weights
        portfolio_returns = simulated_returns @ self.weights
        
        print(f"   Completed {n_simulations:,} simulations")
        print(f"   Each simulation = one random walk path\n")
        
        return portfolio_returns
    
    def generate_time_paths(self, n_paths, n_days, initial_value=10000):
       
        print(f"Generating {n_paths} random walk paths over {n_days} days...")
        
        paths = np.zeros((n_days, n_paths))
        
        for i in range(n_paths):
            # Simulate daily returns for n_days
            daily_returns = np.random.multivariate_normal(
                self.mean_returns,
                self.cov_matrix,
                n_days
            )
            
            # Calculate portfolio returns
            portfolio_daily = daily_returns @ self.weights
            
            # Convert to cumulative value (starting at initial_value)
            paths[:, i] = initial_value * np.cumprod(1 + portfolio_daily)
        
        print(f"  Generated {n_paths} paths\n")
        return paths
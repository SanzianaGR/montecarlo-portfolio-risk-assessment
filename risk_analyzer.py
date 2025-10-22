import numpy as np

class RiskAnalyzer:
    
    @staticmethod
    def calculate_metrics(portfolio_returns):
       
        print(" Calculating Risk Metrics...\n")
        
        stats = {
            # Central tendency
            'mean': np.mean(portfolio_returns),
            'median': np.median(portfolio_returns),
            'std': np.std(portfolio_returns),
            
            # Value at Risk (VaR)
            'var_95': np.percentile(portfolio_returns, 5),   # 5th percentile
            'var_99': np.percentile(portfolio_returns, 1),   # 1st percentile
            
            # Conditional VaR (average of worst cases)
            'cvar_95': portfolio_returns[
                portfolio_returns <= np.percentile(portfolio_returns, 5)
            ].mean(),
            
            # Probabilities
            'prob_loss': np.mean(portfolio_returns < 0),
            'prob_gain': np.mean(portfolio_returns > 0),
            
            # Extremes
            'best_case': np.percentile(portfolio_returns, 95),
            'worst_case': np.percentile(portfolio_returns, 1),
            'max_gain': np.max(portfolio_returns),
            'max_loss': np.min(portfolio_returns)
        }
        
        return stats
    
    @staticmethod
    def print_results(stats, n_simulations):
   
        print("=" * 60)
        print(f"MONTE CARLO RESULTS ({n_simulations:,} simulations)")
        print("=" * 60)
        
        print(f"\nDAILY STATISTICS:")
        print(f"  Expected Return:        {stats['mean']*100:>8.4f}%")
        print(f"  Median Return:          {stats['median']*100:>8.4f}%")
        print(f"  Volatility:             {stats['std']*100:>8.4f}%")
        
        print(f"\nRISK METRICS:")
        print(f"  Value at Risk (95%):    {stats['var_95']*100:>8.4f}%")
        print(f"  Value at Risk (99%):    {stats['var_99']*100:>8.4f}%")
        print(f"  CVaR (95%):             {stats['cvar_95']*100:>8.4f}%")
        
        print(f"\nPROBABILITIES:")
        print(f"  Probability of Loss:    {stats['prob_loss']*100:>8.2f}%")
        print(f"  Probability of Gain:    {stats['prob_gain']*100:>8.2f}%")
        
        print(f"\nEXTREMES:")
        print(f"  Best Simulation:        {stats['max_gain']*100:>8.4f}%")
        print(f"  Worst Simulation:       {stats['max_loss']*100:>8.4f}%")
        
        # Annualized estimates
        annual_return = stats['mean'] * 252
        annual_vol = stats['std'] * np.sqrt(252)
        sharpe = annual_return / annual_vol if annual_vol > 0 else 0
        
        print(f"\nANNUALIZED (252 trading days):")
        print(f"  Expected Return:        {annual_return*100:>8.2f}%")
        print(f"  Volatility:             {annual_vol*100:>8.2f}%")
        print(f"  Sharpe Ratio:           {sharpe:>8.2f}")
        
        print("=" * 60 + "\n")
    
    @staticmethod
    def analyze_paths(paths, initial_value):
      
        final_values = paths[-1, :]
        
        print(f"  PATH ANALYSIS:")
        print(f"  Starting Value:         ${initial_value:>10,.2f}")
        print(f"  Mean Final Value:       ${np.mean(final_values):>10,.2f}")
        print(f"  Median Final Value:     ${np.median(final_values):>10,.2f}")
        print(f"  Best Scenario:          ${np.max(final_values):>10,.2f}")
        print(f"  Worst Scenario:         ${np.min(final_values):>10,.2f}")
        print(f"  % Profitable Paths:     {np.mean(final_values > initial_value)*100:>10.1f}%\n")
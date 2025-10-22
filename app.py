from config import Config
from data_fetcher import DataFetcher
from simulator import MonteCarloSimulator
from risk_analyzer import RiskAnalyzer

def main():
   
    print("STEP 1: Fetching Data")
    print("-" * 60)
    fetcher = DataFetcher(Config.SYMBOLS, Config.HISTORICAL_DAYS)
    returns_df = fetcher.fetch()
    
    if returns_df is None:
        print("✗ Failed to get data. Exiting.")
        return
    
    # STEP 2: Initialize Simulator
    print("\nSTEP 2: Initializing Simulator")
    print("-" * 60)
    simulator = MonteCarloSimulator(returns_df, Config.WEIGHTS)
    
    # STEP 3: Run Simulation
    print("\nSTEP 3: Running Monte Carlo Simulation")
    print("-" * 60)
    portfolio_returns = simulator.run_simulation(Config.N_SIMULATIONS)
    
    # STEP 4: Analyze Results
    print("\nSTEP 4: Analyzing Results")
    print("-" * 60)
    stats = RiskAnalyzer.calculate_metrics(portfolio_returns)
    RiskAnalyzer.print_results(stats, Config.N_SIMULATIONS)
    
    # STEP 5: Generate Time Paths
    print("\nSTEP 5: Generating Random Walk Paths")
    print("-" * 60)
    paths = simulator.generate_time_paths(
        Config.N_PATHS_TO_PLOT,
        Config.HISTORICAL_DAYS,
        Config.INITIAL_INVESTMENT
    )
    RiskAnalyzer.analyze_paths(paths, Config.INITIAL_INVESTMENT)
    

if __name__ == "__main__":
    main()
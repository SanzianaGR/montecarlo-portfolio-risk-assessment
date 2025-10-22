import numpy as np

class Config:
    
    SYMBOLS = ['SPY', 'TLT', 'GLD'] 
    WEIGHTS = np.array([0.4, 0.4, 0.2])  
    
    N_SIMULATIONS = 10000  # number of random walks
    HISTORICAL_DAYS = 252  # 252 trading days in a year (365 - weekends/holidays)
    
    N_PATHS_TO_PLOT = 100  # how many paths to show 
    INITIAL_INVESTMENT = 10000  # Starting portfolio value ($)
    
    
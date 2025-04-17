import pandas as pd

# Example data
asking_prices = pd.Series([10000, 12000, 9000, 15000, 11000])
fair_prices = pd.Series([10500, 11500, 9500, 16000, 12000])

good_deals = asking_prices < fair_prices
good_deal_indices = list(asking_prices[good_deals].index)

print("Good deal indices:", good_deal_indices)
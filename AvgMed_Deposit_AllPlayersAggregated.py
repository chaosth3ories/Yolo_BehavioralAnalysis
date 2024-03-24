import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Avg Median Deposit
average_bet_all_players = data['deposit_usd'].mean()
median_bet_all_players = data['deposit_usd'].median()

# Results
print(f"Average Deposit All Players: {average_bet_all_players}")
print(f"Median Deposit All Players: {median_bet_all_players}")

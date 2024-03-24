import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Total deposits and deposits of winner
total_bet_per_round = data.groupby('roundid')['deposit_usd'].sum()
winner_bet_per_round = data[data['is_winner'] == 1].groupby('roundid')['deposit_usd'].sum()

# Win per round
profit_per_round = total_bet_per_round - winner_bet_per_round

# Avg Median Win per round
average_profit = profit_per_round.mean()
median_profit = profit_per_round.median()

# Highest Lowest Win
max_profit = profit_per_round.max()
min_profit = profit_per_round.min()

# Results
print(f"Average win per round: {average_profit}")
print(f"Median win per round: {median_profit}")
print(f"Highest win per round: {max_profit}")
print(f"Lowest Gwin per rounde: {min_profit}")

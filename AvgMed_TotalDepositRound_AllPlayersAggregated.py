import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Group by round and calc total deposit
total_bet_per_round = data.groupby('roundid')['deposit_usd'].sum()

# Avg Median Deposit per round
average_total_bet_per_round = total_bet_per_round.mean()
median_total_bet_per_round = total_bet_per_round.median()

# Result
print(f"Average Total Deposit per Round: {average_total_bet_per_round}")
print(f"Median Total Deposit per Round: {median_total_bet_per_round}")

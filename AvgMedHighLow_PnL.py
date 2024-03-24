import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# ID Wins Losses
data['result'] = data.apply(lambda row: row['deposit_usd'] if row['is_winner'] == 1 else -row['deposit_usd'], axis=1)

# Total PnL
total_result_per_player = data.groupby('depositor')['result'].sum()

# Avg Median PnL per Player
average_result = total_result_per_player.mean()
median_result = total_result_per_player.median()

# Highest Lowest PnL
max_result = total_result_per_player.max()
min_result = total_result_per_player.min()

# Results
print(f"Avg PnL per player: {average_result}")
print(f"Median PnL per player: {median_result}")
print(f"Highest PnL for one player: {max_result}")
print(f"Lowest PnL for one player: {min_result}")

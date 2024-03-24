import pandas as pd

df = pd.read_csv('DuneMaster.csv')

# Deposit per Player Per Round
deposit_per_round_per_player = df.groupby(['depositor', 'roundid'])['deposit_usd'].sum().reset_index(name='deposit_per_round')

# Average and Median Deposit per Player per Round
deposit_deposit_per_player = deposit_per_round_per_player.groupby('depositor')['deposit_per_round'].mean()
median_deposit_per_player = deposit_per_round_per_player.groupby('depositor')['deposit_per_round'].median()

# Aggregation
average_deposit = deposit_deposit_per_player.mean()
median_deposit = median_deposit_per_player.median()

print(f"Average deposit per round per player: ${average_deposit:.2f}")
print(f"Median deposit per round per player: ${median_deposit:.2f}")

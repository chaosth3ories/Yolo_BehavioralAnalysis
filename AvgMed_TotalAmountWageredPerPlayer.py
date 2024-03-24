import pandas as pd

df = pd.read_csv('DuneMaster.csv')

# Total deposits per player
deposit_per_player = df.groupby('depositor')['deposit_usd'].sum()

# Avg and median deposit per player
avg_deposit = deposit_per_player.mean()
median_deposit = deposit_per_player.median()

print(f"Avg Total Deposit Per Player: ${avg_deposit:.2f}")
print(f"Median Total Deposit Per Player: ${median_deposit:.2f}")

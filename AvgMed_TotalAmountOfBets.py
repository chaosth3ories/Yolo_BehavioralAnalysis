import pandas as pd

df = pd.read_csv('DuneMaster.csv')

# Count of Deposits
deposits_per_player = df.groupby('depositor').size()

# Avg Median Deposits
avg_deposits = deposits_per_player.mean()
median_deposits = deposits_per_player.median()

print(f"Avg Deposits per Player: {avg_deposits:.2f}")
print(f"Median Deposits per player: {median_deposits:.2f}")


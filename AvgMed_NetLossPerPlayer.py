import pandas as pd

df = pd.read_csv('DuneMaster.csv')

# Total Deposit per Round
df['total_deposit_per_round'] = df.groupby('roundid')['deposit_usd'].transform('sum')

# Win per round
df['win_amount'] = df.apply(lambda x: x['total_deposit_per_round'] - x['deposit_usd'] if x['is_winner'] == 1 else 0, axis=1)

# Net loss per player
player_deposit = df.groupby('depositor')['deposit_usd'].sum()
player_wins = df.groupby('depositor')['win_amount'].sum()
netloss_per_player = player_deposit - player_wins

# Avg Median Net Loss
avg_netloss = netloss_per_player.mean()
median_netloss = netloss_per_player.median()

print(f"Durchschnittlicher Nettoverlust pro Spieler: ${avg_netloss:.2f}")
print(f"Medianer Nettoverlust pro Spieler: ${median_netloss:.2f}")

import pandas as pd

df = pd.read_csv('DuneMaster.csv')

# Total deposit per round
df['total_deposit_per_round'] = df.groupby('roundid')['deposit_usd'].transform('sum')

# Win per winround per player
df['win_amount'] = df.apply(lambda x: x['total_deposit_per_round'] - x['deposit_usd'] if x['is_winner'] == 1 else 0, axis=1)

# Net loss
player_deposit = df.groupby('depositor')['deposit_usd'].sum()
player_win = df.groupby('depositor')['win_amount'].sum()
netloss_per_player = player_deposit - player_win

# Percent loss per player
percentloss_per_player = (netloss_per_player / player_deposit) * 100

# avg and median percent loss
avg_percentloss = percentloss_per_player.mean()
median_percentloss = percentloss_per_player.median()

print(f"Avg Percent loss per player: {avg_percentloss:.2f}%")
print(f"Median Percent lsos per player: {median_percentloss:.2f}%")

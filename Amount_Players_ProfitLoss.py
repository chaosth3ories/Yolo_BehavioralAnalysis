import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Profit Loss
data['result'] = data.apply(lambda row: row['deposit_usd'] if row['is_winner'] == 1 else -row['deposit_usd'], axis=1)

# Profit loss per player
total_result_per_player = data.groupby('depositor')['result'].sum()

# Is player in PnL?
players_in_profit = total_result_per_player[total_result_per_player > 0].count()
players_in_loss = total_result_per_player[total_result_per_player < 0].count()

# Results
print(f"Amount of Players in Profit: {players_in_profit}")
print(f"Amount of Players in Loss: {players_in_loss}")

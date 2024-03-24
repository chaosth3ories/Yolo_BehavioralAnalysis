import pandas as pd


data = pd.read_csv('DuneMaster.csv')

# Deposits of Losers per Round
loser_bet_per_round = data[data['is_winner'] == 0].groupby('roundid')['deposit_usd'].sum()

# Losses per round
loss_per_round = loser_bet_per_round

# Avg Median Losses
average_loss = loss_per_round.mean()
median_loss = loss_per_round.median()

# Highest Lowest Loss
max_loss = loss_per_round.max()
min_loss = loss_per_round.min()

# Results
print(f"Average Loss per round: {average_loss}")
print(f"Median loss per round: {median_loss}")
print(f"Highest Loss: {max_loss}")
print(f"Lowest loss: {min_loss}")

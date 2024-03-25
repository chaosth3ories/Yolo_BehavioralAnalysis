import pandas as pd

# Data
data = pd.read_csv('DuneMaster.csv')

#Filter data
non_cancelled_data = data[data['is_too_little_players'] == 0]

# Wins and Losses
number_of_wins = non_cancelled_data[non_cancelled_data['is_winner'] == 1].shape[0]
number_of_losses = non_cancelled_data[non_cancelled_data['is_winner'] == 0].shape[0]

# Results
print(f"Amount of Wins (without cancelled rounds): {number_of_wins}")
print(f"Amount of Losses (without cancelled rounds): {number_of_losses}")


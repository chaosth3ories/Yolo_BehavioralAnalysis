import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Amount of games
total_games = data['roundid'].nunique()

# Unique players
total_players = data['depositor'].nunique()

# Cancelled rounds
aborted_rounds = data['is_too_little_players'].sum()

# Unclaimed wins
unclaimed_wins = data['is_unclaimed'].sum()

# Total volume
total_volume_eth = data['deposit_eth'].sum()
total_volume_usd = data['deposit_usd'].sum()

# Results
print(f"Amount of games: {total_games}")
print(f"Amount of players: {total_players}")
print(f"Cancelled games: {aborted_rounds}")
print(f"Unclaimed wins: {unclaimed_wins}")
print(f"Volume in ETH: {total_volume_eth}")
print(f"Volume in USD: {total_volume_usd}")

import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Amount Cancelled games
aborted_games_count = data['is_too_little_players'].sum()

# Count players
players_in_aborted_games = data[data['is_too_little_players'] == 1]['depositor'].nunique()

# Unique players
total_unique_players = data['depositor'].nunique()

# Percentage of players in cancelled games
percentage_players_in_aborted_games = (players_in_aborted_games / total_unique_players) * 100

# Results
print(f"Amount of cancelled games: {aborted_games_count}")
print(f"Amount of unique players in cancelled games: {players_in_aborted_games}")
print(f"Percentage of players in cancelled games: {percentage_players_in_aborted_games:.2f}%")

import pandas as pd

df = pd.read_csv('DuneMaster.csv')

# Rounds per player
round_count_per_player = df['depositor'].value_counts()

# Max player
max_games = round_count_per_player.max()
player_with_max_rounds = round_count_per_player[round_count_per_player == max_games]

print("Player with max rounds:")
print(player_with_max_rounds)
print(f"Amount of rounds: {max_games}")

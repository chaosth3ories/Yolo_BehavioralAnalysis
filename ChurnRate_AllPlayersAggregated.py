import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# ID Players and Rounds
rounds_per_player = data.groupby('depositor')['roundid'].nunique()

# Count 1 game players
one_round_players = rounds_per_player[rounds_per_player == 1].count()

# Unique players
total_unique_players = rounds_per_player.count()

# CR
churn_rate = (one_round_players / total_unique_players) * 100

# Results
print(f"Churn Rate: {churn_rate:.2f}%")

import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Rounds per player
sessions_per_player = data.groupby('depositor')['roundid'].nunique()

# Avg Median rounds per player
average_sessions_per_player = sessions_per_player.mean()
median_sessions_per_player = sessions_per_player.median()

# Results
print(f"Average rounds per player: {average_sessions_per_player:.2f}")
print(f"Median rounds per player: {median_sessions_per_player:.2f}")


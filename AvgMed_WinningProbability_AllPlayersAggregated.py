import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Total deposit per round
total_bets_per_round = data.groupby('roundid')['deposit_usd'].sum()

# Total deposits to individual rounds
data['total_bet_round'] = data['roundid'].map(total_bets_per_round)

# Win Probability Individual
data['win_probability'] = data['deposit_usd'] / data['total_bet_round']

# Avg Med Win Probability
average_probability = data['win_probability'].mean()
median_probability = data['win_probability'].median()

# Results
print(f"Average Winning Probability: {average_probability}")
print(f"Median Winning Probability: {median_probability}")


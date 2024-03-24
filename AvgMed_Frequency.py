import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Change date
data['date'] = pd.to_datetime(data['block_time']).dt.date

# First bet last bet
first_bet_date = data.groupby('depositor')['date'].min()
last_bet_date = data.groupby('depositor')['date'].max()

# Betting period
betting_period_days = (last_bet_date - first_bet_date).apply(lambda x: x.days) + 1

## Betting days
unique_betting_days_per_player = data.groupby('depositor')['date'].nunique()

# Percentage
percentage_of_active_betting_days = (unique_betting_days_per_player / betting_period_days) * 100

# Avg Median
average_percentage_of_active_betting_days = percentage_of_active_betting_days.mean()
median_percentage_of_active_betting_days = percentage_of_active_betting_days.median()

# Results
print(f"Average Frequency: {average_percentage_of_active_betting_days:.2f}%")
print(f"Median Frequency: {median_percentage_of_active_betting_days:.2f}%")
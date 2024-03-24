import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('DuneMaster.csv')  

# Change date
data['block_time'] = pd.to_datetime(data['block_time'], utc=True)

data['hour'] = data['block_time'].dt.hour

# Players per hour
players_per_hour = data.groupby('hour')['depositor'].nunique()

# Deposit per player per round
data['total_deposits_per_player_round'] = data.groupby(['roundid', 'depositor'])['deposit_usd'].transform('sum')

# Avg
data['avg_deposit_per_round'] = data.groupby('roundid')['total_deposits_per_player_round'].transform('mean')

# Avg per hour
avg_deposit_per_hour = data.groupby('hour')['avg_deposit_per_round'].mean()

# Plot
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(players_per_hour.index, players_per_hour, color='blue', label='Number of Players')
ax1.set_xlabel('Hour of the Day (UTC)')
ax1.set_ylabel('Number of Players', color='blue')
ax1.tick_params('y', colors='blue')

ax2 = ax1.twinx()
ax2.plot(avg_deposit_per_hour.index, avg_deposit_per_hour, color='red', marker='o', label='Average Deposit (USD)')
ax2.set_ylabel('Average Deposit per Round (USD)', color='red')
ax2.tick_params('y', colors='red')

# Legend
plt.title('Player Activity and Average Betting Amount per Hour')
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()

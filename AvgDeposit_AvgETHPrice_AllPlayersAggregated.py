import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


data = pd.read_csv('DuneMaster.csv')

# Change date
data['date'] = pd.to_datetime(data['block_time']).dt.date

# ETH Price
data['eth_price'] = data['deposit_usd'] / data['deposit_eth']

# ETH deposit and price
average_deposit_per_day = data.groupby('date')['deposit_usd'].mean()
average_price_per_day = data.groupby('date')['eth_price'].mean()

# Plot
fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Average Bet Size in USD', color=color)
ax1.plot(average_deposit_per_day.index, average_deposit_per_day, color=color)
ax1.tick_params(axis='y', labelcolor=color)


ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Average ETH in USD Price', color=color)
ax2.plot(average_price_per_day.index, average_price_per_day, color=color)
ax2.tick_params(axis='y', labelcolor=color)

# Formating
ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

fig.tight_layout()  # adjust layout
plt.title('Average Betting Size in USD - Average ETH price')
plt.show()

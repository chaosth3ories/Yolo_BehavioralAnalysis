import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Change
data['date'] = pd.to_datetime(data['block_time']).dt.date

# Total Deposit per player
total_amount_wagered_per_player = data.groupby('depositor')['deposit_usd'].sum()

# Top 5% filter
top_5_percent_threshold = total_amount_wagered_per_player.quantile(0.95)
top_5_percent_players = total_amount_wagered_per_player[total_amount_wagered_per_player >= top_5_percent_threshold].index

top_5_percent_data = data[data['depositor'].isin(top_5_percent_players)].copy()

# Duration
first_bet_date = top_5_percent_data.groupby('depositor')['date'].min()
last_bet_date = top_5_percent_data.groupby('depositor')['date'].max()
betting_duration_days = (last_bet_date - first_bet_date).apply(lambda x: x.days)

# Avg and Median duration
average_betting_duration = betting_duration_days.mean()
median_betting_duration = betting_duration_days.median()

# Avg and Median total amount wagered
average_total_amount_wagered = total_amount_wagered_per_player[top_5_percent_players].mean()
median_total_amount_wagered = total_amount_wagered_per_player[top_5_percent_players].median()

# Avg and Median deposit per round
average_deposit_usd_per_round_top_5_percent = top_5_percent_data.groupby('roundid')['deposit_usd'].mean().mean()
median_deposit_usd_per_round_top_5_percent = top_5_percent_data.groupby('roundid')['deposit_usd'].median().median()

# PnL
top_5_percent_data['profit_loss_usd'] = top_5_percent_data.apply(lambda x: x['deposit_usd'] if x['is_winner'] == 1 else -x['deposit_usd'], axis=1)
average_profit_loss_top_5_percent = top_5_percent_data['profit_loss_usd'].mean()
median_profit_loss_top_5_percent = top_5_percent_data['profit_loss_usd'].median()

# Avg and Median rounds played
average_rounds_played_top_5_percent = top_5_percent_data.groupby('depositor')['roundid'].nunique().mean()
median_rounds_played_top_5_percent = top_5_percent_data.groupby('depositor')['roundid'].nunique().median()

# Amount players
number_of_top_5_percent_players = len(top_5_percent_players)

# Results
print(f"Amount of Players Top 5%: {number_of_top_5_percent_players}")
print(f"Avg Duration: {average_betting_duration}")
print(f"Median Duration: {median_betting_duration}")
print(f"Average total amount wagered Top 5% player in USD: {average_total_amount_wagered}")
print(f"Median total amount wagered Top 5% player in USD: {median_total_amount_wagered}")
print(f"Avg Deposit per round of Top 5%: {average_deposit_usd_per_round_top_5_percent}")
print(f"Median Deposit per round of Top 5%: {median_deposit_usd_per_round_top_5_percent}")
print(f"Avg PnL Top 5%: {average_profit_loss_top_5_percent}")
print(f"Median PnL Top 5%: {median_profit_loss_top_5_percent}")
print(f"Avg played rounds Top 5% player: {average_rounds_played_top_5_percent}")
print(f"Median played rounds top 5% player: {median_rounds_played_top_5_percent}")


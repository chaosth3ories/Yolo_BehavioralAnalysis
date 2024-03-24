import pandas as pd

data = pd.read_csv('DuneMaster.csv')

# Filter data
players_with_ens = data[~data['ens_name'].isna() & (data['ens_name'] != '')]

# Count players
unique_players_with_ens = players_with_ens['depositor'].nunique()

# Results
print(f"Amount of Players with an ENS-Name: {unique_players_with_ens}")

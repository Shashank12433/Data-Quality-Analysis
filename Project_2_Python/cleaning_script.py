import pandas as pd

# Load data
df = pd.read_csv('dirty_data.csv')

# 1. Handle Missing Values
df['category'] = df['category'].fillna('Unknown')
df = df.dropna(subset=['signup_date']) # Drop if date is entirely missing

# 2. Standardize Dates
df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')

# 3. Standardize Categories (State)
state_mapping = {'new york': 'NY', 'ny': 'NY', 'ca': 'CA', 'tx': 'TX', 'texas': 'TX'}
df['state'] = df['state'].str.strip().str.lower().map(state_mapping).fillna(df['state'].str.upper().str.strip())
df['category'] = df['category'].str.title()

# 4. Remove Duplicates
df = df.drop_duplicates()

# Export clean dataset
df.to_csv('cleaned_data.csv', index=False)
print("Data cleaned successfully.")

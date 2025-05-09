import pandas as pd
import os

df = pd.read_csv(os.path.join("dataset", "data.csv"))

incorrect_rows = df[df['Pulse'] > df['Maxpulse']]
print("🔍 Incorrect rows (Pulse > Maxpulse):")
print(incorrect_rows)

condition = df['Pulse'] > df['Maxpulse']
df.loc[condition, ['Pulse', 'Maxpulse']] = df.loc[condition, ['Maxpulse', 'Pulse']].values

# Confirm fix
print("\n✅ Fixed rows:")
print(df.loc[condition])

df.to_csv('/data/data_fixed.csv', index=False)
print("\n💾 Cleaned data saved as 'data_fixed.csv'")

import pandas as pd

# Sample schedule
df = pd.DataFrame({
    'John': [True, False, True, True, False, False, True, False, True, False],
    'Judy': [True, False, False, True, False, True, True, False, False, True]
})

# Party happens when both John and Judy are present
df['party'] = df['John'] & df['Judy']

# Initialize days_til_party with the same length
days_til_party = [None] * len(df)

# Traverse backwards to calculate days till next party
next_party_day = None
for i in reversed(range(len(df))):
    if df.loc[i, 'party']:
        next_party_day = i
        days_til_party[i] = 0
    elif next_party_day is not None:
        days_til_party[i] = next_party_day - i
    else:
        days_til_party[i] = None

df['days_til_party'] = days_til_party
print(df)

import pandas as pd
import itertools

# Example dataset
df = pd.DataFrame({
    'artist': ['A', 'A', 'B', 'B', 'A'],
    'venue': ['X', 'X', 'Y', 'Z', 'Y'],
    'date': pd.to_datetime(['2022-01-05', '2022-01-20', '2022-01-05', '2022-02-15', '2022-01-25'])
})

# Extract year-month
df['year_month'] = df['date'].dt.to_period('M').astype(str)

# Cross product of all unique (artist, venue) pairs
artists = df['artist'].unique()
venues = df['venue'].unique()
artist_venue_pairs = pd.MultiIndex.from_tuples(list(itertools.product(artists, venues)), names=['artist', 'venue'])

# Group by year_month, artist, venue and count
grouped = df.groupby(['year_month', 'artist', 'venue']).size().reindex(
    pd.MultiIndex.from_product([df['year_month'].unique(), artist_venue_pairs], names=['year_month', 'artist', 'venue']),
    fill_value=0
)

# Reshape to wide format
result = grouped.unstack(['artist', 'venue']).fillna(0).astype(int)
print(result)
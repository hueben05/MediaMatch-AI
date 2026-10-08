import pandas as pd
df = pd.read_csv('data/raw/anime_metadata.csv')
orig_df = pd.read_csv('data/cleaned/anime_cleaned.csv')
print(df[["id","title","genres","titleEn"]].head())

new_csv_ids = df["id"]
orig_csv_ids = orig_df["anime_id"]


match_mask = orig_csv_ids.isin(new_csv_ids)
count = match_mask.sum()
unmatched_df = orig_df[~match_mask]

total_anime = len(orig_df)
unmatched = len(orig_df) - count
coverage = (count/total_anime) * 100
print(f"Total Amt of Anime: {total_anime}")
print(f"Unmatched Anime: {unmatched}")
print(f"Coverage Percentage: {coverage}%")

print(unmatched_df.head())



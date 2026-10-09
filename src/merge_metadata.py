import pandas as pd
df = pd.read_csv('data/raw/anime_metadata.csv')
orig_df = pd.read_csv('data/cleaned/anime_cleaned.csv')
#print(df[["id","title","genres","titleEn"]].head())

new_csv_ids = df["id"]
orig_csv_ids = orig_df["anime_id"]


match_mask = orig_csv_ids.isin(new_csv_ids)
count = match_mask.sum()
unmatched_df = orig_df[~match_mask]

total_anime = len(orig_df)
unmatched = len(orig_df) - count
coverage = (count/total_anime) * 100
#print(f"Total Amt of Anime: {total_anime}")
#print(f"Unmatched Anime: {unmatched}")
#print(f"Coverage Percentage: {coverage}%")

#print(unmatched_df.head())


missing_genres = df["genres"].isnull().sum()
missing_titleEn = df["titleEn"].isnull().sum()

new_df = df[["id","genres","titleEn"]]
new_df = new_df.rename(columns={"id": "anime_id"})

merged_df = orig_df.merge(new_df, on="anime_id", how="left")

orig_rows = len(orig_df)
merged_rows = len(merged_df)
print(orig_rows, merged_rows)

print(merged_df[["anime_id","title","genres","titleEn"]].head())

merged_df.to_csv("data/cleaned/anime_with_metadata.csv")
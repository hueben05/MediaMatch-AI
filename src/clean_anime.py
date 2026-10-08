import pandas as pd
df = pd.read_csv('data/raw/anime.csv')
# ------ Data Exploration (Debug/Learning) ------
print(df.head())
print("\nDataset shape: ", df.shape)
print("Column names: ", df.columns)
df.info()
print("Missing info: ", df.isnull().sum())
print("\nDescribe: ", df.describe())

# ------ Data Cleaning ------
new_df = df.drop("image_url", axis = 1)
print("New_df Columns:\n", new_df.columns)

#Dropping rows with missing values
new_df = new_df.dropna(subset=["synopsis","start_date"])

#Fill missing episodes with the median
ep_median = new_df["episodes"].median()
new_df["episodes"] = new_df["episodes"].fillna(ep_median)

#Making sure its clean
print(new_df["episodes"].isnull().sum())

#Saving it to a clean file
new_df.to_csv("data/cleaned/anime_cleaned.csv", index=False)
print(list(df.columns))

print((df[["anime_id","title"]]).head())

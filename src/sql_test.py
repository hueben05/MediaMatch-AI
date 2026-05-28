import sqlite3
import pandas as pd

#Connect to database
db_connection = sqlite3.connect("data/anime.db")

# Load cleaned dataset
cleaned_anime_df = pd.read_csv("data/cleaned/anime_cleaned.csv")

# Save DataFrame to SQL table
cleaned_anime_df.to_sql("anime",db_connection, if_exists="replace",index=False)

#Create a cursor to run SQL queries
db_cursor = db_connection.cursor()

# Execute SQL query
#db_cursor.execute("SELECT * FROM anime LIMIT 5;")

# Fetch results
#query_results = db_cursor.fetchall()

# Print results
#print(query_results)

db_cursor.execute("""
SELECT title, score
FROM anime
WHERE score > 8
ORDER BY score DESC
LIMIT 10;
""")
new_results = db_cursor.fetchall()
print(new_results)

db_cursor.execute("""
SELECT COUNT(*)
FROM anime
WHERE score > 8              
""")
count_result = db_cursor.fetchone()
print(count_result[0])

db_cursor.execute("""
SELECT type, AVG(score)
FROM anime
GROUP BY type
""")
avg_results = db_cursor.fetchall()
print(avg_results)
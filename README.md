# MediaMatch AI

MediaMatch AI is an AI-powered anime recommendation system.

The goal of this project is to build a recommendation engine that suggests anime based on content, popularity, and user-relevant features using machine learning techniques.

## Level 1: Data Pipeline

In Level 1, I worked with a real-world anime dataset and focused on preparing it for analysis and machine learning.

### What I Built

* Loaded and explored a 10,000-row anime dataset using Pandas
* Inspected data types, missing values, and dataset statistics
* Removed unnecessary columns like `image_url`
* Dropped rows missing critical data such as `synopsis`
* Filled missing `episodes` values using the median
* Saved the cleaned dataset to a new CSV file
* Created a SQLite database from the cleaned dataset
* Queried the database using SQL

### Technologies Used

* Python
* Pandas
* SQLite
* SQL

### SQL Concepts Practiced

* `SELECT`
* `WHERE`
* `ORDER BY`
* `LIMIT`
* `COUNT`
* `GROUP BY`
* `AVG`

### What I Learned

* How to clean and prepare messy real-world data
* The difference between dropping rows and filling missing values
* Why median is sometimes better than mean for handling outliers
* How Pandas and SQL solve similar data problems in different ways
* How data moves through a pipeline:

Raw CSV → Cleaned DataFrame → SQLite Database → SQL Queries

### Future Goals

Future levels of this project will include:

* Machine learning recommendation models
* Clustering and rating prediction
* LLM integration
* FastAPI backend development
* Cloud deployment

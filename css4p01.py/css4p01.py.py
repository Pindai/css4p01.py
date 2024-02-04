# importing data

import pandas as pd

movie_data = pd.read_csv("movie_dataset.csv")

print(movie_data)

print(movie_data.info())

print(movie_data.describe)

print(movie_data["Rating"].max())

#%%
# removing the NaN from the data

x = movie_data["Revenue (Millions)"].mean()

movie_data["Revenue (Millions)"].fillna(x, inplace = True)

y = movie_data["Metascore"].mean()

movie_data["Metascore"].fillna(y, inplace = True)

print(movie_data["Revenue (Millions)"].mean())

#%%
# Use boolean indexing to select movies directed by the specific years
revenue = movie_data[movie_data["Year"] >= 2015]

# Calculate the average revenue of movies
average_revenue = revenue["Revenue (Millions)"].mean()

# Display the result
print("The average revenue of movies:", average_revenue)

#%%

# Count the number of movies released in '2016' in the 'Year' column
count_2016 = (movie_data["Year"] == 2016).sum()

# Display the result
print("Number of movies released in 2016:", count_2016)

#%%
# Count the number of movies directed by Christopher Noah
Nolan = (movie_data["Director"] == "Christopher Nolan").sum()

# Display the result
print("Number of movies directed by Christopher Nolan:", Nolan)

#%%

# Count the number of movies that have a rating of at least 8.0
rating = (movie_data["Rating"] >= 8.0).sum()

# Display the result
print("Number of movies that have a rating of at least 8.0:", rating)
#%%

# Use boolean indexing to select movies directed by the specific author
directed = movie_data[movie_data["Director"] == "Christopher Nolan"]

# Calculate the average rating
average_rating = directed["Rating"].mean()

# Display the result
print("Average Rating:", average_rating)

#%%

# fitering movies that was released on a specific year
rate2006 = movie_data[movie_data["Year"] == 2006]
rate2007 = movie_data[movie_data["Year"] == 2007]
rate2008 = movie_data[movie_data["Year"] == 2008]
rate2016 = movie_data[movie_data["Year"] == 2016]

# Calculate the average rating per specified year
average_rating2006 = rate2006["Rating"].mean()
average_rating2007 = rate2007["Rating"].mean()
average_rating2008 = rate2008["Rating"].mean()
average_rating2016 = rate2016["Rating"].mean()



# Display the result
print("Average Rating for the year 2006:", average_rating2006)
print("Average Rating for the year 2007:", average_rating2007)
print("Average Rating for the year 2008:", average_rating2008)
print("Average Rating for the year 2016:", average_rating2016)


#%%

# Count the number of movies produced in each year
movie_counts = movie_data['Year'].value_counts().sort_index()

# Get the movie counts for the specified years
count_year1 = movie_counts.get(2006, 0)
count_year2 = movie_counts.get(2016, 0)

# Calculate the percentage increase
percentage_increase = ((count_year2 - count_year1) / count_year1) * 100

# Display the result
print(f"Number of movies in {2006}: {count_year1}")
print(f"Number of movies in {2016}: {count_year2}")
print(f"Percentage increase: {percentage_increase:.2f}%")

#%%

from collections import Counter

# Split the names in each cell and create a list of all names
all_names = [name.strip() for names in movie_data["Actors"].str.split(",") for name in names]

# Count the occurrences of each name
name_counts = Counter(all_names)

# Identify the most common name
most_appearing_name = name_counts.most_common(1)[0][0]

# Display the result
print("Most appearing name:", most_appearing_name)

#%% 

# Split the genres in each cell and create a list of all genres
all_genres = [genre.strip() for genres in movie_data["Genre"].str.split(",") for genre in genres]

# Count the occurrences of each genre
genre_counts = Counter(all_genres)

# Display the result
print("Genre counts:", len(genre_counts))

#%%

# Specify the columns for correlation analysis
columns_of_interest = ["Year", "Runtime (Minutes)", "Rating" , "Votes", "Revenue (Millions)","Metascore"]

# Calculate the correlation matrix
correlation_matrix = movie_data[columns_of_interest].corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

import seaborn as sns
import matplotlib.pyplot as plt

# Plotting the correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title("Correlation Heatmap")
plt.show()

#%%
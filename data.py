import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('IMDB-Movie-Data.csv')

#Which year has the highest revenue?
data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)
sns.barplot(x='Year', y='Revenue (Millions)', data=data)
plt.title("Revenue By Year")
plt.show()

# Average rating for each director in descending order

print(data.groupby('Director')['Rating'].mean().sort_values(ascending=False))

#Most popular movie by revenue
print(data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]['Title'])

#Top 10 Highest Rated Movie Titles and its Directors
top10_len=data.nlargest(10, 'Rating') [['Title', 'Rating', 'Director']].set_index('Title')

sns.barplot(x='Rating', y=top10_len.index, data=top10_len,hue='Director', dodge=False)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()

#Top 10 highest revenue movie titles

top_10 = data.nlargest(10, 'Revenue (Millions)')[['Title', 'Revenue (Millions)']].set_index('Title')
sns.barplot(x='Revenue (Millions)', y=top_10.index, data=top_10)
plt.title('Top 10 Highest Revenue Movie Titles')
plt.show()
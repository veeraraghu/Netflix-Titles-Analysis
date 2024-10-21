# -*- coding: utf-8 -*-

#Necessary libraries were imported
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading Netflix titles data
netflix = pd.read_csv('netflix_titles.csv')
print(netflix.head(), '\n')

#Finding number of titkes released per year
release_year = netflix.groupby('release_year')['title'].count()
print('Number of titles released yearly')
print(release_year, '\n')

#Creating a Dashboard
fig = plt.figure(figsize=(16, 12))
plt.title('Netflix Titles Analysis', fontsize=30)
plt.axis('off')

#Forming a Grid to plot outputs in a single plot
grid = plt.GridSpec(12, 16, hspace=0.75, wspace=0.75)

#Name and Student ID
ax = fig.add_subplot(grid[0:1, :])
text = '''Name: Veera Raghunatha Reddy Naguru
Student Id: 22028322'''
ax.text(0.5, 0, text, fontsize=18, ha='center')
ax.axis('off')

#Plotting Number of movies released per year
ax1 = fig.add_subplot(grid[1:5, 0:5])
ax1.plot(release_year.index, release_year, color='m',
         label='Number of Titles')
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Movies')
ax1.set_title('Yearly Releases', fontsize=14)
ax1.legend()

ax2 = fig.add_subplot(grid[1:5, 4:9])
text = '''
  We can see a sudden increase
in number of titles released
per year from 2000 and it
got a decline from 2018.

About 1147 titles released
in year 2018.

More than 1000 titles were
released in 2017,2018 and
2019 individually.
'''
ax2.text(0.5, 0, text, fontsize=13, ha='center')
ax2.axis('off')

#Type of titles count
netflix_type = netflix.groupby('type')['title'].count()
print('Movies and TV Shows count')
print(netflix_type, '\n')

#Plotting Number of titles in Movies and TV Shows
ax3 = fig.add_subplot(grid[1:5, 8:13])
ax3.pie(netflix_type, labels=netflix_type.index, autopct='%1.1f%%')
ax3.set_title('%Type of titles', fontsize=14)

ax4 = fig.add_subplot(grid[1:5, 12:])
text = '''
Out of 8807 titles released in
Netflix, 6131 titles that is 
69.6% are Movies and 2676 titles
that is 30.4% are TV Shows.

TV Shows duration in Netflix are
rangng from 1 Season to 
17 Seasons.
'''
ax4.text(0.5, 0.1, text, fontsize=13, ha='center')
ax4.axis('off')

#Country wise number of titles released
country = netflix.groupby('country')['title'].count()
country = country.sort_values(ascending=False)
country_10 = country.head(10)
print(country_10)

#Plotting top 10 countries with highest number of titles released
ax5 = fig.add_subplot(grid[6:10, 0:5])
bars = ax5.barh(country_10.index, country_10, color='g')
ax5.bar_label(bars, label_type='edge', rotation=90, size='small', padding=2)
ax5.set_title('Top 10 Country wise number of titles')
ax5.set_xlabel('Number of titles')
ax5.set_ylabel('Country')

ax6 = fig.add_subplot(grid[5:9, 5:9])
text = '''
We can see that 2818 titles
were released in United States.

972 titles were released in India.

It can be seen that less than 500
titles were released in the top 
10 Countries with highest number 
of title releases.
'''
ax6.text(0.5, -0.1, text, fontsize=13, ha='center')
ax6.axis('off')

#Titles in each rating
rating = netflix.groupby('rating')['title'].count()
rating = rating.iloc[5:-2]

#Plotting Number of titles for each Rating
ax7 = fig.add_subplot(grid[5:9, 10:15])
bars = ax7.bar(rating.index, rating, color='b')
ax7.set_xticks(rating.index)
ax7.set_xticklabels(rating.index, rotation=90)
ax7.bar_label(bars, size='x-small')
ax7.set_title('Movies per Rating')
ax7.set_xlabel('Rating')
ax7.set_ylabel('Number of titles')

ax8 = fig.add_subplot(grid[10:12, 9:])
text = '''
We can see that Netflix titles are 
classified into 10 Ratings.
Most titles are rated as TV-14 and TV-PG.
Out of total titles only 80 titles were
rated NR which is Not Rated.
'''
ax8.text(0.5, 0.3, text, fontsize=13, ha='center')
ax8.axis('off')

ax9 = fig.add_subplot(grid[10:, :8])
text = '''
We can see that titles were released in Netflix from 1925.
More % of titles released were Movies but including episodes of TV Shows
it is most likely to change the statistics.
'''
ax9.text(0.5, 0, text, fontsize=13, ha='center')
ax9.axis('off')

plt.savefig('22028322.png', bbox_inches='tight', dpi=300)
plt.show()

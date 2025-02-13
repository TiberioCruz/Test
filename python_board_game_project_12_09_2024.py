# -*- coding: utf-8 -*-
"""Python Board Game Project 12/09/2024.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oFHUQGoaCIzjvY-20uEWkreJqJUCVzaz

# Import Lib
"""

import pandas as pd
import plotly.express as px

"""# Import files"""

df_gamers = pd.read_csv('/content/gamers.csv')
#Clean gamers
df_gamers = df_gamers[['country', 'region', 'population', 'casual_gamers', 'serious_gamers']]

df_games = pd.read_csv('/content/games.csv')

df_gamers = pd.read_csv('/content/gamers.csv')

df_themes = pd.read_csv('/content/themes.csv')

df_mechanics = pd.read_csv('/content/mechanics.csv')

df_artists_reduced = pd.read_csv('/content/artists_reduced.csv')

df_designers_reduced = pd.read_csv('designers_reduced.csv')

df_users_ratings = pd.read_csv('/content/user_ratings.csv')

"""# Explore Date - Top 10s

"""

# Top 10 games by ranking
df_games[['BGGId','Name','Rank:boardgame']].sort_values("Rank:boardgame")[0:10]

# Top 10 most popula game themes
# Generate the bar chart
fig = px.bar(
    df_themes.drop(columns='BGGId').sum().sort_values(ascending=False)[0:10],
    text_auto=True
)

# Update the chart layout
fig.update_layout(
    title="Most Popular Game Themes",
    xaxis_title="Themes",
    yaxis_title="Count",
    showlegend=False
)

# Show the chart
fig.show()

# Top 10 most popula game mechanics
# Generate the bar chart
fig = px.bar(
    df_mechanics.drop(columns='BGGId').sum().sort_values(ascending=False)[0:10],
    text_auto=True
)

# Update the chart layout
fig.update_layout(
    title="Most Popular Mechanics",
    xaxis_title="Mechanics",
    yaxis_title="Count",
    showlegend=False
)

# Show the chart
fig.show()

"""# Serious and Casual gamers distribuition by Country"""

# Create percentage of gamers
df_gamers['casual_gamers_percent'] = ((df_gamers['casual_gamers'] / df_gamers['population']) * 100).round(1)
df_gamers['serious_gamers_percent'] = ((df_gamers['serious_gamers'] / df_gamers['population']) * 100).round(1)

px.bar(df_gamers.sort_values("casual_gamers", ascending = False)[0:20], x = 'country', y = 'casual_gamers', text_auto = True)

px.bar(df_gamers.sort_values("casual_gamers_percent", ascending = False)[0:20], x = 'country', y = 'casual_gamers_percent')

px.bar(df_gamers.sort_values("serious_gamers", ascending = False)[0:20], x = 'country', y = 'serious_gamers', text_auto = True)

px.bar(df_gamers.sort_values("serious_gamers_percent", ascending = False)[0:20], x = 'country', y = 'serious_gamers_percent')

"""# Demand for the different types of games in the countries"""

df_games[['BGGId','Name','NumOwned','NumWant','NumWish']].sort_values("NumWish", ascending=False)





"""# Top Artists and Designers"""

df_artists_reduced.head()

# Top 10 Artists
# Generate the bar chart
fig = px.bar(
    df_artists_reduced.drop(columns = ["BGGId","Low-Exp Artist", "(Uncredited)"]).sum().sort_values(ascending=False)[0:10],
    text_auto=True
)

# Update the chart layout
fig.update_layout(
    title="Top 10 Artists",
    xaxis_title="Artists",
    yaxis_title="Count",
    showlegend=False
)

# Show the chart
fig.show()

# Top 10 Designers
# Generate the bar chart
fig = px.bar(
    df_designers_reduced.drop(columns = ["BGGId","Low-Exp Designer", "(Uncredited)"]).sum().sort_values(ascending=False)[0:10],
    text_auto=True
)

# Update the chart layout
fig.update_layout(
    title="Top 10 Designers",
    xaxis_title="Designers",
    yaxis_title="Count",
    showlegend=False
)

# Show the chart
fig.show()

df_gamers.head()

df_games.head()
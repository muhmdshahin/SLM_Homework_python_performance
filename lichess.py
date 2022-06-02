import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from statsmodels.nonparametric.smoothers_lowess import lowess as  sm_lowess
df = pd.read_csv('puzzles.csv')
df.columns = ["PuzzleId", "FEN", "Moves", "Rating", "RatingDeviation", "Popularity", "NbPlays", "Themes", "GameUrl"]
plays_lo = statistics.median(df["NbPlays"])

rating_lo = 1500
rating_hi = np.quantile(df["Rating"], 0.99)


good = df[(df["Rating"] > rating_lo) & (df["Rating"] < rating_hi) & (df["NbPlays"] > plays_lo)][["Rating", "Popularity"]]


rating_mapping = defaultdict(list)
for (i, rating) in enumerate(good['Rating'].values):
    rating_mapping[rating].append(i)

ratings = good['Rating'].unique()
mean_popularities = []

for rating in ratings:
    indices = rating_mapping[rating]
    popularities = good.iloc[indices, good.columns.get_loc("Popularity")]
    mean_popularities.append(statistics.mean(popularities))

print(ratings.size)
print(len(mean_popularities))
plt.scatter(ratings, mean_popularities)
sm_y, sm_x = sm_lowess(ratings, mean_popularities, frac=0.25, it=5, return_sorted=True).T
plt.plot(sm_x,sm_y,color="red")
plt.xlabel = "Rating"
plt.ylabel = "Popularity"
plt.show()

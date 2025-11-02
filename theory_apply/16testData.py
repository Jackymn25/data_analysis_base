# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

"""
Case: A test grade dataset of a classroom in a school is shown  as follows,
finish the follwing Tasks:

- calculate each students' total grade and avg grade
- find students with above 90 in math and above 85 is english
- rank the whole dataset by total score, priority is given to math then science,
 give the top 3 students
- 
"""

data = pd.read_csv("students_scores_named.csv")
print(data.head(3))
scores = pd.DataFrame(data)

# Task1
print(scores[['math','science','English']].sum(axis=1))
scores['Total Grade'] = scores[['math','science','English']].sum(axis=1)
scores['Avg'] = scores[['math','science','English']].mean(axis=1)
print(scores.head())

# Task2
print(scores[(scores.math>=90)&(scores.English>=85)])

# Task3
print(scores.sort_values(by=['Total Grade', 'math', 'science'], ascending = False))
score_ranked = scores.sort_values(by=['Total Grade', 'math', 'science'], ascending = False)
print(score_ranked.nlargest(3, columns=['Total Grade', 'math', 'science']))

# Task 4
ranked = scores.sort_values(
    by=['Total Grade','math','science'],
    ascending=False,
    kind='mergesort'
)
ranks = pd.Series(np.arange(1, len(ranked)+1), index=ranked.index, name='Rank')
scores['Rank'] = ranks
print(scores)

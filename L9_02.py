import pandas as pd
import numpy as np
# sample code
table = [
    ['A', 'Noah', 90, 92],
    ['B', 'Liam', 81, 83],
    ['C', 'William', 87,85],
    ['B', 'Benjamin.', 82,80],
    ['A', 'Emma.', 90,94],
    ['C', 'Olivia', 50,60],
    ['A', 'Isabella', 70,71],
    ['C', 'Amelia', 84,86],
    ['B', 'Mia', 88,85],
]
df = pd.DataFrame(table,columns = ['class', 'name', 'math_score', 'eng_score'])
# print(something) # total score
class_sum = df.groupby('class').sum()
print(class_sum)
print('-'*20)
# print(something) # mean score
class_mean = df.groupby('class').mean()
print(class_mean)
print('-'*20)
# print(something) # correlation coefficient
corr = df.corr()
print("corr: ")
print(corr)
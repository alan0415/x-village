import pandas as pd

pets = ['Labrador Retriever', 'Beagle', 'Dachshund', 'Shiba Inu']
pets_index = ['Alex', 'Alice', 'Neo', 'Kenny']
series_1 = pd.Series(pets,index=pets_index)
print(series_1)
print('-'*20)
print(series_1[0])
print('-'*20)
print(series_1[[0,1,2]])
print('-'*20)
print(series_1['Alex'])
print('-'*20)
print(series_1[['Alex','Alice']])
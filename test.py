import numpy as np
import pandas as pd


column_names=['class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium',
              'Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins',
              'Color intensity','Hue','Diluted wines','Proline']

wines = pd.read_csv('wine.csv',names=column_names)

wineclasses = wines['class']


del wines['class']

wines['petrol'] = wines['Malic acid']*2


list1 = [[1,2,3],[4,5,5]]
        



arrays = [
    [1,2,3],
    [11,22,33],
    [111,222,333]
    ]

tuples = list(zip(*arrays))

print(tuples)
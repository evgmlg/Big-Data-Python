import pandas as pd
import numpy as np

from sklearn.decomposition import PCA

#Задание 1
close_prices = pd.read_csv('close_prices.csv')

#Задание 2
close_prices = close_prices.drop('date', axis=1)
pca = PCA(n_components=10)
pca.fit(close_prices)

cumulative_explained_variance = np.cumsum(pca.explained_variance_ratio_)
num_components = np.where(cumulative_explained_variance >= 0.9)[0][0] + 1
print(f"Количество компонентнов, достаточных для объяснения 90-процентной дисперсии: {num_components}")

#Задание 3
data_transformed = pca.transform(close_prices)
first_component = data_transformed[:, 0]

#Задание 4
djia_index = pd.read_csv('djia_index.csv')
correlation = round(pd.Series(first_component).corr(djia_index['^DJI']),2)
print(f"Корреляция Пирсона между первой компонентой и индексом Доу-Джонса: {correlation}")

#Задание 5
weights = pd.Series(pca.components_[0], index=close_prices.columns)
max_weight = weights.max()
company = weights[weights == max_weight].index[0]
print('Компания, имеющая наибольший вес в первой компоненте:', company)

import numpy as np
import pandas as pd

# Pandas - расширение NumPy (Структурные массивы)

# Series, DataFrame, Index - основы

## Series

# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data, type(data))

# print(data.values, data.index)

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print(data['a'])
# print(data['b':'d'])

# population_dict = {
#     'city1' : 1001,
#     'city2' : 1002,
#     'city3' : 1003
# }

# population = pd.Series(population_dict)
# print(population)

# Для создания Series можно использовать: списки и массивы NumPy, скаляры, словари 

## DataFrame - двумерный массив с явно опреленными индексами. Последовательность "согласованных" Series'oв

# population_dict = {
#     'city1' : 1001,
#     'city2' : 1002,
#     'city3' : 1003
# }

# area_dict = {
#     'city1' : 200000,
#     'city2' : 300000,
#     'city3' : 500000,
# }

# population = pd.Series(population_dict)
# area = pd.Series(area_dict)

# print(population)
# print(area)

# states = pd.DataFrame({
#     'population' : population,
#     'area' : area
# })

# print(states)

# print(states['area'])

# ind = pd.Index([1, 2, 5, 7, 11])
# print(ind[::2])

# indA = pd.Index([1, 2, 3, 4, 5])
# indB = pd.Index([2, 3, 4, 5, 6])

# print(indA.intersection(indB))

# Выборка данных из Series
#как словарь

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

# print('a' in data)
# print(data.keys())

# data['a'] = 100
# data['z'] = 1000
# print(data)

# # Series как одномерный массив

# print(data['a':'c'])
# print(data[(data > 0.5) & (data < 1)])
# print(data[['a', 'd']])

# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=[1, 3, 10, 25])

# print(data.loc[1], data.iloc[1])

#Выборка из DataFrame

# population_dict = {
#     'city1' : 1001,
#     'city2' : 1002,
#     'city3' : 1003
# }

# area_dict = {
#     'city1' : 200000,
#     'city2' : 300000,
#     'city3' : 500000,
# }

# population = pd.Series(population_dict)
# area = pd.Series(area_dict)

# data = pd.DataFrame({'area': area, 'population' : population})

# print(data['area'])

# data['new'] = data['area']

# print(data)

# # двумерный NumPy-массив

# print(data)
# print(data.T)
# print(data['area'])

# print(data.values[0:3])

# #атрибуты-индикаторы

# print(data.iloc[:3, 1:2])
# print(data.loc[:'city2', 'area' : 'population'])

# data.iloc[0, 1] = 99999
# print(data)

# rng = np.random.default_rng()
# s = pd.Series(rng.integers(0,10,4))

# print(s)
# print(np.exp(s))

# population_dict = {
#     'city1' : 1001,
#     'city2' : 1002,
#     'city3' : 1003,
#     'city42' : 1004
# }

# area_dict = {
#     'city1' : 200000,
#     'city2' : 300000,
#     'city3' : 500000,
#     'city41' : 600000
# }

# population = pd.Series(population_dict)
# area = pd.Series(area_dict)

# data = pd.DataFrame({'area': area, 'population' : population})

# print(data)

# dfa = pd.DataFrame(rng.integers(0,10, (2,2)), columns=['a', 'b'])

# dfb = pd.DataFrame(rng.integers(0,10, (3,3)), columns=['a', 'b', 'c'])

# print(dfa, dfb, dfa + dfb)

# rng = np.random.default_rng(1)

# a = rng.integers(0,10, (3,4))
# print(a)
# print(a[0])

# print(a - a[0])

# df = pd.DataFrame(a, columns=['a', 'b', 'c', 'd'])

# print(df)
# print(df - df.iloc[0, ::2])

# NA - значение: NaN, null

# Два способа хранения NA
# 1. индикаторы NaN, None
# 2. null

# None - объект

val1 = np.array([1, 2, 3])
print(val1.sum())

val1 = np.array([1, np.nan, 2, 3])
print(np.nansum(val1))



x = pd.Series(range(10), dtype=int)
print(x)

x[0] = None
x[1] = np.nan

print(x)

x1 = pd.Series(['a', 'b', 'c'])
x1[0] = None
x1[1] = np.nan
print(x1)

x2 = pd.Series([1,2,3, np.nan, None, pd.NA], dtype='Int32')
print(x2)

print(x2.isnull())
print(x2.dropna())

df = pd.DataFrame([
    [1,2,3, np.nan, None, pd.NA],
    [1,2,3, None, 5, 6],
    [1, np.nan,3, None, 5, 6]
])

print(df)
print(df.dropna(axis=1))

# - all - все значения NA, any - хотя бы одно, thresh = x 

print(df.dropna(axis=1, how='all'))
print(df.dropna(axis=1, how='any'))
print(df.dropna(axis=1, thresh=2))
import numpy as np
import pandas as pd

# Если размерность данных >2, то используют иерархическую индексацию. В один индекс включается несколько уровней

# index = [
#     ('city1', 2010),
#     ('city1', 2020),
#     ('city2', 2010),
#     ('city2', 2020),
#     ('city3', 2010),
#     ('city3', 2020),
# ]

# population = [101, 201, 102, 202, 103, 203]

# pop = pd.Series(population, index = index)
# print(pop)

# #print(pop[[i for i in pop.index if i[1] == 2020]])

# # MultiIndex

# index = pd.MultiIndex.from_tuples(index)
# pop = pop.reindex(index)
# print(pop)
# print(pop[:, 2020])

# pop_df = pop.unstack()
# print(pop_df)
# print(pop_df.stack())

# index = [
#     ('city1', 2010, 1),
#     ('city1', 2010, 2),

#     ('city1', 2020, 1),
#     ('city1', 2020, 2),

#     ('city2', 2010, 1),
#     ('city2', 2010, 2),

#     ('city2', 2020, 1),
#     ('city2', 2020, 2),

#     ('city3', 2010, 1),
#     ('city3', 2010, 2),

#     ('city3', 2020, 1),
#     ('city3', 2020, 2),
# ]

# population = [101, 1010, 201, 2010,  102, 1020, 202, 2020, 103, 1030, 203, 2030]

# pop = pd.Series(population, index = index)
# print(pop)

# index = pd.MultiIndex.from_tuples(index)
# pop = pop.reindex(index)
# print(pop[:, :, 2])

# pop_df = pop.unstack()
# print(pop_df)

# pop_df = pd.DataFrame({
#     'total': pop,
#     'something': [101, 1010, 201, 2010,  102, 1020, 202, 2020, 103, 1030, 203, 2030]
# })

# print(pop_df)
# print(pop_df['something'])

# pop_df1 = pop_df.loc['city1', 'something']
# print(pop_df1)

## Создание мультииндексов

# 1 - список массивов, задающих значения индекса на каждом уровне

# i = pd.MultiIndex.from_arrays([
#     ['a', 'a', 'b', 'b'],
#     [1, 2, 1, 2]
# ])

# print(i)

# # 2 - Список кортежей

# i2 = pd.MultiIndex.from_tuples([
#     ('a', 1),
#     ('a', 2),
#     ('b', 1),
#     ('b', 2)
# ])
# print(i2)

# # 3 - Декартого произведение индексов
# i3 = pd.MultiIndex.from_product([
#     ['a', 'b'],
#     [1, 2]
# ])
# print(i3)

# # 4 - Описание внутреннего представления: levels, codes
# i4 = pd.MultiIndex(
#     levels=[
#         ['a', 'b'],
#         [1, 2]
#     ],
#     codes=[
#         [0, 0, 1, 1], # a a b b
#         [0, 1, 0, 1]  # 1 2 1 2
#     ]
# )
# print(i4)

# Задание названия уровням

# data = {
#     ('city_1', 2010): 100,
#     ('city_1', 2020): 200,
#     ('city_2', 2010): 1001,
#     ('city_2', 2020): 2001,
# }

# s = pd.Series(data)
# print(s)
# s.index.names = ['city', 'year']
# print(s)

# index = pd.MultiIndex.from_product([
#     ['city1', 'city2'],
#     [2010, 2020]
#     ], 
#     names=['city', 'year']
# )
# print(index)

# columns = pd.MultiIndex.from_product([
#     ['person1', 'person2', 'person3'],
#     ['job1', 'job2']
#     ], 
#     names=['worker', 'job']
# )

# rng = np.random.default_rng(1)

# data = rng.random((4, 6))

# print(data)

# data_df = pd.DataFrame(data, index=index, columns=columns)
# print(data_df)

# ## Индексация и срезы (по мультииндексу)

# data = {
#     ('city_1', 2010): 100,
#     ('city_1', 2020): 200,
#     ('city_2', 2010): 1001,
#     ('city_2', 2020): 2001,
#     ('city_3', 2010): 10001,
#     ('city_3', 2020): 20001,
# }

# s = pd.Series(data)
# s.index.names = ['city', 'year']

# print(s['city_1', 2010])
# print(s['city_1'])
# print(s.loc['city_1':'city_2'])

# print(s[s > 2000])

# Перегруппировка мультииндексов

# rng = np.random.default_rng(1)

# data = rng.random(6)

# index = pd.MultiIndex.from_product([
#     ['a', 'c', 'b'],
#     [1, 2]
# ])

# data = pd.Series(data, index=index)
# data.index.names = ['char', 'int']
# print(data)
# #print(data['a':'b'])

# data = data.sort_index()
# print(data['a':'b'])

index = [
    ('city1', 2010, 1),
    ('city1', 2010, 2),

    ('city1', 2020, 1),
    ('city1', 2020, 2),

    ('city2', 2010, 1),
    ('city2', 2010, 2),

    ('city2', 2020, 1),
    ('city2', 2020, 2),

    ('city3', 2010, 1),
    ('city3', 2010, 2),

    ('city3', 2020, 1),
    ('city3', 2020, 2),
]

population = [101, 1010, 201, 2010,  102, 1020, 202, 2020, 103, 1030, 203, 2030]

pop = pd.Series(population, index = index)

i = pd.MultiIndex.from_tuples(index)

pop = pop.reindex(i)
print(pop.unstack())
print(pop.unstack(level=0))
print(pop.unstack(level=1))
print(pop.unstack(level=2))

# NumPy конкатенация

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]

print(np.concatenate([x, y, z]))

x = [[1, 2, 3]]
y = [[4, 5, 6]]
z = [[7, 8, 9]]

print(np.concatenate([x, y, z]))

ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
ser2 = pd.Series(['d', 'e', 'f'], index=[1,2,6])
print(pd.concat([ser1, ser2], verify_integrity=False))
print(pd.concat([ser1, ser2], ignore_index=True))
print(pd.concat([ser1, ser2], keys=['x', 'y']))

ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
ser2 = pd.Series(['d', 'e', 'f'], index=[4,5,6])

print(pd.concat([ser1, ser2], join='outer'))
print(pd.concat([ser1, ser2], join='inner'))
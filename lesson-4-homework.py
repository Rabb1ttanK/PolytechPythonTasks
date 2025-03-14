import pandas as pd
import numpy as np

# 1. Разобраться как использовать мультииндексные ключи в данном примере
index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]
index = pd.MultiIndex.from_tuples(index)
pop = pd.Series(population, index = index)
pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)
pop_df_1 = pop_df.loc['city_1', 'something']
print(pop_df_1)
pop_df_1 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]
print('\n', pop_df_1)
pop_df_1 = pop_df.loc[['city_1', 'city_3'], 'something']
print('\n', pop_df_1)



# 2. Из получившихся данных выбрать данные по 
index = pd.MultiIndex.from_product([
    ['city1', 'city2'],
    [2010, 2020]
    ], 
    names=['city', 'year']
)
print(index)

columns = pd.MultiIndex.from_product([
    ['person1', 'person2', 'person3'],
    ['job1', 'job2']
    ], 
    names=['worker', 'job']
)

rng = np.random.default_rng(1)

data = rng.random((4, 6))

print(data)

data_df = pd.DataFrame(data, index=index, columns=columns)
print(data_df)

# - 2020 году (для всех столбцов)
print(data_df.loc[:, 2020, :])

# - job_1 (для всех строк)
print(data_df.xs('job1', axis=1, level=1))

# - для city_1 и job_2 

print(data_df.loc['city1'].xs('job1', axis=1, level=1))


# 3. Взять за основу DataFrame со следующей структурой
index = pd.MultiIndex.from_product(
    [
        ['city_1', 'city_2'],
        [2010, 2020]
    ],
    names=['city', 'year']
)
columns = pd.MultiIndex.from_product(
    [
        ['person_1', 'person_2', 'person_3'],
        ['job_1', 'job_2']
    ],
    names=['worker', 'job']
)

data = rng.random((4, 6))
data_df = pd.DataFrame(data, index=index, columns=columns)


# Выполнить запрос на получение следующих данных
# - все данные по person_1 и person_3
print(data_df.loc[:, ['person_1','person_3']])

# - все данные по первому городу и первым двум person-ам (с использование срезов)
print(data_df.loc['city_1', 'person_2':'person_3'])

# Приведите пример (самостоятельно) с использованием pd.IndexSlice
print(data_df.loc[pd.IndexSlice[:, ['person_1', 'person_2']]])


#4. Привести пример использования inner и outer джойнов для Series (данные примера скорее всего нужно изменить)
ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
ser2 = pd.Series(['b', 'c', 'f'], index=[1, 2, 3])
df1 = pd.DataFrame([ser1, ser2])
ser2 = pd.Series(['b', 'c', 'f'], index=[1, 2, 4])
df2 = pd.DataFrame([ser2, ser2])

print (pd.concat([df1, df2], join='outer'))
print (pd.concat([df1, df2], join='inner'))

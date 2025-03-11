import numpy as np
import pandas as pd


# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
# - скалярные значение
# - словари

list = [1, 2, 3, 4]
a = pd.Series(list)
print(a)
nparr = np.arange(10)
b = pd.Series(nparr)
print(b)
c = pd.Series([4, 12, 2.3])
print(c)
car_dict = {
    'BMW' : 'X5',
    'VolksWagen' : 'Beetle',
    'Lada' : 'Niva'
}
d = pd.Series(car_dict)
print(d)

# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
population_dict = {
    'city1' : 1001,
    'city2' : 1002,
    'city3' : 1003
}

area_dict = {
    'city1' : 200000,
    'city2' : 300000,
    'city3' : 500000,
}

population = pd.Series(population_dict)
area = pd.Series(area_dict)


print(population)
print(area)

states = pd.DataFrame({
    'population' : population,
    'area' : area
})
# - списки словарей
list = [population_dict, area_dict]
states2 = pd.DataFrame(list)

print(states2)

# - словари объектов Series

dict = {"poulation": population, "area": area}

print(pd.DataFrame(dict))

# - двумерный массив NumPy

array = np.array([
    ['AMD', 'Intel', 'nvidea', 'SUN'],
    ['Ryezen', 'Core', "Geforce", 'Sparc']
])

print(pd.DataFrame(array))
# - структурированный массив Numpy

a = np.array([('Sana', 2, 21.0), ('Mansi', 7, 29.0)],  
       dtype=[('name', (np.str_, 10)), ('age', np.int32), ('weight', np.float64)]) 

print(pd.DataFrame(a))

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1

population_dict = {
    'city1' : 1001,
    'city2' : 1002,
    'city3' : 1003,
    'city42' : 1004
}

area_dict = {
    'city1' : 200000,
    'city2' : 300000,
    'city3' : 500000,
    'city41' : 600000
}

population = pd.Series(population_dict)
area = pd.Series(area_dict)

data = pd.DataFrame({'area': area, 'population' : population}).fillna(1)

print(data)

# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ

rng = np.random.default_rng(1)

a = rng.integers(0,10, (3,4))
print(a)
print(a[0])

print(a - a[0])

df = pd.DataFrame(a, columns=['a', 'b', 'c', 'd'])

print(df)
print(df.subtract(df.iloc[:, 0], axis=0))

# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()

df = pd.DataFrame([
    [1,2,3, np.nan, None, pd.NA],
    [1,2,3, None, 5, 6],
    [1, np.nan,3, None, 5, 6]
])

print('\n', df.ffill())
print(df.bfill())
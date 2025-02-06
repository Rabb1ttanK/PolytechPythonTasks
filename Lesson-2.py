import numpy as np

# # Суммирование значений в массиве

# rng = np.random.default_rng(1)
# s = rng.random(50)

# print(s)
# print(np.sum(s))

# a = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ])

# print(np.sum(a))
# print(np.sum(a, axis=0))
# print(np.sum(a, axis=1))

# print(np.min(a, axis=0))

# # NaN = Not a Number
# print(np.nanmax(a))

# Транслирование (broadcasting)
# Набор правил которые позволяют осуществлять бинарные операции с массивами разных форм и размеров

# a = np.array([0, 1, 2])
# b = np.array([5, 5, 5])

# print(a+b)
# print(a+5)

# # 5 транслируется в [5, 5, 5], т.e. подстраивается по размер массива a

# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# print(a+5)

# a = np.array([0, 1, 2])
# b = np.array([[0], [1], [2]])

# print(a+b)

# # Правила
# # 1. Если размерности массива отличаются, то форма матрицы с меньшей размерностью дополняется 1 с левой стороны
# # 2. Если формы не совпадают в каком-то измерении, то если у массива форма равна 1, то он растягивается до соответствия формы второго массива
# # 3. Если после применения этих правил в каком либо измерении размеры отличаются и ни один из них не равен 1, то транслирование невозможно

# a = np.array([[0, 1, 2], [3, 4, 5]])
# b = np.array([5])

# print(np.ndim(a), a.shape, b.shape)

# # b(1,) -> b(1, 1)
# #b(1,1) -> (1,1) -> (2,3)


# print(a+b)

# a = np.ones((2,3))
# b = np.arange(3)

# print(a, b)

# print(np.ndim(a), a.shape, b.ndim, b.shape)

# # (2, 3)  (2, 3)    (2, 3)
# # (3,) -> (1, 3) -> (2, 3)

# print(a+b)

# a = np.arange(3).reshape((3,1))
# b = np.arange(3)

# print(a, b)

# print(a.ndim, a.shape, b.ndim, b.shape)

# # (3, 1)   (3, 1) -> (3, 3)
# # (3,)  -> (1, 3) -> (3, 3)

# print(a+b)

# a = np.ones((3,2))
# b = np.arange(3)

# #2 (3,2)   (3, 2)    (3, 2)
# #1 (3,) -> (1, 3) -> (3, 3)


# x = np.array([
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [9, 8, 7, 6, 5, 4, 3, 2, 1]
# ])

# xmean0 = x.mean(0)

# print(xmean0)

# xcent0 = x - xmean0

# print(xcent0)

# xmean1 = x.mean(1)
# print(xmean1)

# xmean1 = xmean1[:, np.newaxis]
# xcent1 = x - xmean1

# print(xcent1)

# x = np.linspace(0, 5, 50)
# y = np.linspace(0, 5, 50)[:, np.newaxis]

# z = np.sin(x) ** 3 + np.cos(20+y*x) * np.sin(y)

# print(z.shape)

# import matplotlib.pyplot as plt

# plt.imshow(z)
# plt.colorbar()
# plt.show()

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ])

# print(x < 3)
# print(np.less(x, 3))

# print(np.sum(x < 3))
# print(np.sum(y < 4, axis=1))

# x = np.array([1, 2, 3, 4, 5])
# print(x[x < 3])

# Векторизация индекса

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# index = [1, 5, 7]
# print(x[index]) 

# index = [[1, 5, 7], [2, 4, 8]]

# print(x[index])

# x = np.arange(12).reshape(3, 4)

# print(x)
# print(x[1:, [2, 0, 1]])

# x = np.arange(10)
# i = np.array([2, 1, 8, 4])

# print(x)

# x[i] = 999
# print(x)

# ## Сортировка

# x = [3, 4, 2, 6, 2, 8, 5, 0, 3]
# print(np.sort(x))

data = np.zeros(4, dtype= {
    'names':(
        'name', 'age'
    ),
    'formats':(
        'U10', 'i4'
    )
})

print(data.dtype)

name = ['a', 'b', 'c', 'd']
age = [1, 2, 3, 4]
data['name'] = name
data['age'] = age

print(data)

# Массивы записей

data_rec = data.view(np.recarray)
print(data_rec)
print(data_rec[0])
import numpy as np
import sys
import array

#Типы данных Python

# x = 1
# print(type(x))
# print(sys.getsizeof(x))

# x = True
# print(type(x))

# l1 = list([])
# print(sys.getsizeof(l1))

# l2 = list([1, 2, 3])
# print(sys.getsizeof(l2))

# l3 = list([1, "2", True])
# print(sys.getsizeof(l3))

# a1 = array.array('i', [1, 2, 3])
# print(sys.getsizeof(a1), " ", type(a1))

# # a = np.array([1, 2, 3, 4, 5])
# # print(type(a), a)

# #Повышающее приведение типов
# a = np.array([1.23, 2, 3, 4, 5])
# print(type(a), a)

# a = np.array([1.23, 2, 3, 4, 5], dtype=int)
# print(type(a), a)

# a = np.array([range(i, i+3) for i in [2, 4, 6]])
# print(a)

# a = np.zeros(10, dtype=int)
# print(a, type(a))

# print(np.ones((3,5), dtype=float))

# print(np.full((4,5), 3.12354))

# print(np.arange(0, 20, 2))

# print(np.eye(4))



# np.random.seed(1)

# x1 = np.random.randint(10, size=3)

# print(x1)

# x2 = np.random.randint(10, size=(3, 2))
# print(x2)

# x3 = np.random.randint(10, size=(3,2,1))
# print(x3)

# print(x1.ndim, x1.shape, x1.size)
# print(x2.ndim, x2.shape, x2.size)
# print(x3.ndim, x3.shape, x3.size)

#Индекс (с 0)

# a = np.array([1,2,3,4,5])
# print(a[0])
# print(a[-2])

# a[1] = 20

# print(a)

# a = np.array([[1,2], [3,4]])
# print(a[-1,-1])

# a[1, 0] = 100
# print(a)

# a = np.array([1, 2, 3, 4])
# b = np.array([1.0, 2, 3, 4])

# print(a)
# print(b)

# a[0] = 10

# print(a)

# a[0] = 1.2
# print(a) 

## Срез [s:f:st] [0:shape:1]

# a = np.array([1,2,3,4,5,6])
# print(a[:3])

# print(a[3:])

# print(a[::-1])



# x = np.array([1, 2, 3])
# y = np.array([4, 5, 7])
# z = np.array([6])

# print(np.concatenate([x, y, z]))

# r1 = np.vstack([x, y])
# print(r1)

# print(np.hstack([r1, r1]))



### Вычисление массивов

# Векторезированная операция

# x = np.arange(10)

# print(x)

# print(x*2 + 1)

# # Универсальные функции

# print(np.add(np.multiply(x,2), 1)) # == print(x*2 + 1)

# # - / // ** % - Операторы универсальных функций

# ## np.abs, sin/cos/tan, exp, log, - другие универсальные функции

# x = np.arange(5)

# y = np.zeros(10)

# print(np.multiply(x, 10, out=y[::2]))

# print(y)

# x = np.arange(1, 5)
# print(x)

# print(np.add.accumulate(x))

# x = np.arange(1, 10)

# print(np.add.outer(x, x))
# print(np.multiply.outer(x, x))
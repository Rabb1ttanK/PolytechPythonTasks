import numpy as np
import sys
import array

# 1. Какие еще существуют коды типов?

    # «c» — тип символа;
    # «b» — подписанный символ, тип int;
    # «B» — без подписи символ, тип int;
    # «u» — тип символа Юникода;
    # «h» — подписанный короткий тип int;
    # «H» — без подписи короткий тип int;
    # «i» — подписанный тип int, тип int;
    # «I» — без подписи тип int, тип long;
    # «l» — подписанный длинный тип int, тип long;
    # «L» — без подписи длинный тип long;
    # «f» — тип float, тип float;
    # «d» — тип double, тип float, 8 байт.

# # 2. Напишите код, подобный приведенному выше, но другим типам

# x = 10.22

# print(type(x))
# print(sys.getsizeof(x))

# x = "Hello world"

# print(type(x))
# print(sys.getsizeof(x))

# arr = array.array('f', [1, 11.11, 12.24])

# print(sys.getsizeof(arr), " ", type(arr))

# # 3. Напишите код для создания массива с 5 значениями, распологающимися через равные интервалы в диапозоне от 0 до 1

# a1 = np.arange(0, 1, 0.2)
# print(a1)

# ## 4. Напишите код для создания массива с 5 равномерно распределенными случайными значениями в диапазоне от 0 до 1

# ran_num = np.random.random()

# ran_dist = np.random.random() * 0.2

# a2 = np.arange(ran_num, 1, ran_dist, dtype=float)

# print(a2)

# ## 5. Напишите код для создания массива с 5 нормально распределенными случайными значениями с мат. ожиданием = 0 и дисперсией 1

# a3 = np.random.normal(0, 1, 5)

# print(a3)

# ## 6. Напишите код для создания массива с 5 случайнвми целыми числами в от [0, 10)

# a4 = [np.random.randint(1, 10) for x in range(10)]

# print(a4)

# ## 7. Написать код для срезов массива 3х4

# arr = np.random.randint(10, size=(3,4))

# ## - первые две строки и три столбца

# print(arr)

# print(arr[:2, :3])

# ## - первые три строки и второй столбец

# print(arr[:3, 1:2])

# ## - все строки и столбцы в обратном порядке

# print(arr[::-1, ::-1])

# ## - второй столбец

# print(arr[:3, 1:2])

# # - третья строка

# print(arr[2:3, :4])

# ## 8. Продемонстрируйте, как сделать срез-копию

# a = [1, 2, 3]
# b = a[::1]

# b[0] = 100
# print(a, " ", b)

# a = np.arange(1, 13)

# print(a)
# print(a.reshape(2,6))

# ## 9. Продемонстрируйте использование newaxis для получения вектора-столбца и вектора-строки

# a = np.arange(1, 4)
# row = a[np.newaxis, :]
# print(row)
# col = a[:, np.newaxis]
# print(col)

# ## 10. Разберитесь, как работает метод dstack

# x = np.arange(1, 10)
# y = np.arange(1,10)

# r1 = np.vstack([x, y])

# x = x[np.newaxis, :]
# y = y[np.newaxis, :]

# print(np.dstack([x, y]))
# print(np.dstack([r1, r1]))

# ## 11. Разберитесь, как работают методы split, vsplit, hsplit, dsplit

# print(np.vsplit(r1, 1))

# x = [1, 2, 3]
# y = [4, 5, 6]
# z = np.concatenate([x, y])
# print(z, '\n', np.split(z, 2))
# print(np.hsplit(z, 3))
# z = np.dstack([x, y])
# print(z, '\n', np.dsplit(z, 2))

## 12. Привести пример использования всех универсальных функций, которые я привел

x = np.arange(10)

print(x//2)

print(x%3)

print(x/7)

print(x**5)

# Рассчет последовательности Фибоначчи рекурсивно

def fib_recursive(n):
    if n in (1, 2):
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)
    
print(fib_recursive(10), ' ')

# Рассчет последовательности Фибоначчи итеративно

def fib_iterative(n):
    fib0 = 0
    fib1 = 1
    for i in range(2, n+1):
        fib0, fib1 = fib1, fib1 + fib0
    return fib1

print(fib_iterative(10), ' ')

# Рассчет последовательности Фибоначчи матрично

def multiply_matrices(a,b):
    zip_b = zip(*b)
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]


def matrix_power(n, M):
     if n == 1:
          return M
     elif n == 2:
          return multiply_matrices(M, M)
     elif n // 2 == 0:
          n = n/2
          return multiply_matrices(matrix_power(n,  M), matrix_power(n, M))
     else:
          return multiply_matrices(M, matrix_power(n - 1, M))
     
def fib_matrix(n):
    M = [[1,1], [1,0]]
    M = matrix_power(n, M)
    return M[0][1]

print (fib_matrix(10))
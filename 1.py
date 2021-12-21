import time
import math
from typing import final


"""    20.09.21    """
def check1(A, B):
    """линейная функция"""
    if A ==  0 and B != 0:
        return False
    elif A == 0 and B ==0:
        return True
    elif A != 0:
        return -(B/A)

def check2(A, B, C):
    """квадратичная функция"""

    if A == 0:
        return check1(B, C)

    def D(A, B, C):
        """нахождение дискриминанта"""
        return (B**2) - (4*A*C)
        
    d =  D(A,B,C) 

    if d > 0:
        x1 = (-B + math.sqrt(d)) / (2*A)
        x2 = (-B - math.sqrt(d)) / (2*A)
        return x1, x2

    elif d == 0:
        return -B / (2*A)
    
    else:
        x1 = (-B + math.sqrt(-d)) / (2*A)
        x2 = (-B - math.sqrt(-d)) / (2*A)

        return complex(x1, 1), complex(x2, 1)
        # return f"i+{x1}", f"i+{x2}"

ABSOLUTE_ERROR = 0.000001
def sqrt(A):
    """нахождение корня"""
    x0 = A/2
    x1 = 0.5*(x0 + (A/x0))
    print(x1)
    if not abs(x1 - x0) >= ABSOLUTE_ERROR:
        sqrt(x1)
    
    return x1
# print(sqrt(36))

def resheto(n):
    """решето эратосфена"""
    if n < 2: return False
    
    res = []
    for i in range(2, n):
        flag = False
    
        for a in res:
            if not i%a: flag = True
    
        if not flag: res.append(i)
    
    return res

# start = time.time()
# for i in resheto(10000):
#     print(i)
# finish = time.time()
# print(finish-start)

# import time

# def eratalgo(n):
#   mass = list(range(n + 1))
#   mass[1] = 0    
#   for i in mass:
#     if i > 1:
#       for j in range(i + i, len(mass), i):
#         mass[j] = 0
#   return mass

# start = time.time()
# eratalgo(1000)
# finish = time.time()
# print(finish-start)




"""    27.09.21    """
def iter_factorial(n):
    """факториал (итрационный)"""
    res = 1
    for i in range(1, n+1): res *= i
    return res
# print(iter_factorial(156))

def rec_factorial(n, res=1):
    """факториал (рекурсивный)"""
    res *= n
    if n == 1: return res
    return rec_factorial(n-1, res)
# print(rec_factorial(156))

def rec_2_factorial(n, res=1):
    """факториал (рекурсивный 2)"""
    res *= n
    if n <= 2: return res
    return rec_2_factorial(n-2, res)

# start = time.time()
# rec_2_factorial(1000)
# finish = time.time()
# print(finish-start)

import math
def func_2(n):
    x = range(1, rec_2_factorial(n)+1)
    res = 0
    for i in range(1, n+1):
        res += x[i-1]/math.e**i
    return res

# print(rec_2_factorial(1))
# print(math.e**1)
# print(1/math.e)

# start = time.time()
# func_2(100)
# finish = time.time()
# print(finish-start)

def generatePascaltriangle(numRows):
    """посторение треугольника Паскаля"""
    result = []
    for i in range(numRows):
        result.append([1])
        for j in range(i):
            if j != i-1:
                result[i].append(result[i-1][j]+result[i-1][j+1])
            else:
                result[i].append(1)
    return result
# [print(i) for i in generatePascaltriangle(10)]


"""    28.09.21    """
MEMO = {}
def fibo(n):
    """Число фибоначи"""
    if n<0: return False
    if n == 1: return 0
    if n == 2: return 1
    if n in MEMO: return MEMO[n]
    if n-1 in MEMO and n-2 in MEMO: return MEMO[n-1]+MEMO[n-2]
    if n-2 in MEMO: return fibo(n-1) + MEMO[n-2]
    if n-1 in MEMO: return MEMO[n-1] + fibo(n-2)
    MEMO[n] = fibo(n-1)+fibo(n-2)

    return MEMO[n]
# num = 1000
# for i in range(num+1):
#     print(i, fibo(i))

""" 04.10.21 """
# def nod(a, b):
#     res = []
#     print(res)
#     if not a%2:
#         res.append(a%2)
#         nod(a%2, b)
#     else:
#         return a
#     if not b%2:
#         res.append(b%2)
#         nod(a, b%2)
#     else:
#         return b
#     return res
# print(nod(12, 4))

def nod(a, b):
    """НОД 2 чисел"""
    if a == b: return a
    if a > b:
        return nod(a-b, b)
    else:
        return nod(a, b-a)

def start(inputs):
    """НОД нескольких чисел"""
    a = inputs.pop(0)
    b = inputs.pop(0)
    if inputs:
        inputs.insert(0, nod(a, b))
        return start(inputs)
    return nod(a, b)
# print(start([3, 10, 3, 2, 1]))

def line_search(arr, target):
    """линейный поиск"""
    for i in arr:
        if target == i: return True
    return False

def binary_search(arr, target):
    """бинарный поиск"""
    while arr:
        mid = len(arr) // 2
        if target == arr[mid]: return True
        if len(arr) <= 2: return False
        if target > arr[mid]: arr = arr[mid:]
        elif target < arr[mid]: arr = arr[:mid]
# target = int(input("Введите число для поиска: "))
# arr = [int(i) for i in input("Введите последовательность чисел через пробел: ").split()]
# from datetime import datetime; timer = datetime.now
# start_line = timer(); line_search(arr, target); final_line = timer()
# start_binary = timer(); binary_search(arr, target); final_binary = timer()
# print("Время выполнения линейного поиска: ", final_line-start_line)
# print("Время выполнения бинарного поиска: ", final_binary-start_binary)
# # target: 10
# # arr: -45 -58 -37 -33 -21 -20 -18 -13 -12 -5 -3 0 2 3 5 7 9 10


""" 21.12.21 """
def create():
    """создание последовательности"""
    n=input("Введите число:\n")
    import random
    return [random.randint(1, 1000) for i in range(int(n))]

def alg(arr):
    """нахождение возрастающей подпоследовательности максимальной длины"""
    print("array =",arr)
    arrays = []
    sub_arr = []
    for i in arr:
        if not sub_arr:
            sub_arr.append(i)
            continue
        if i >= sub_arr[-1]:
            sub_arr.append(i)
        else:
            arrays.append(sub_arr)
            sub_arr = [i]    
    arrays.append(sub_arr)
    if len(arr) == 1: return arr
    if not arrays or not arrays[0]: return []
    return max(arrays, key=lambda x: len(x))
# while True:
#     print("res =", alg(create()))

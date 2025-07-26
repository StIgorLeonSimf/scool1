"""Рекурсия"""

# def num2(n):
#     if n > 1:
#         num2(n-1)
#     print(n)
# def num1(n):
#     if n > 1:
#         num2(n-1)
#     print(n)
# def num(n):
#     if n > -2:
#         num(n-1)
#     print(n)
#
# num(5)
import math

"""
3! = 1*2*3 = 3 * 2!
2! = 1* 2  = 2 * 1!
1! = 1

n! = n * (n-1)!
"""

#
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# print(fact(6))
# factt = list(range(2, 7))
# print(math.prod(factt))

# ls = [1, 2, [3, 4, [5, [6, 7, 8]]]]
#
# def summ(l):
#     cnt = 0
#     for i in l:
#         if type(i) != list:
#             cnt += i
#         else:
#             cnt += summ(i)
#     return cnt
#
# print(summ(ls))

"""
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

n(f) = (n-1)f + (n-2)f 
"""

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(9))

"""Замыкания"""

def name(nm):
    cnt = 0
    def surname(snm):
        # global cnt
        nonlocal cnt
        cnt += 1
        print(cnt, nm, snm)
    return surname
cnt = 1000
sur = name('Marry')
sur('Petrova')
sur('Ivanova')
sur('Sidorova')
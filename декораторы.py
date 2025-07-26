import random
import time
from functools import wraps


def time_run(func):
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        stop = time.perf_counter()
        duration = stop - start
        print(f'Время выполнения функции {func.__name__} '
              f'- {duration:.2f} cек.')
    return wrap


def in_out(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f'На входе функции {func.__name__} - {args}, {kwargs}')
        res = func(*args, **kwargs)
        print(f'На выходе функции {func.__name__} - {res}')
        return res + 1000
    return wrap


def decor(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper

@decor
def proba():
    print('PROBA')


@time_run
def etalon(n, m):
    print('START')
    time.sleep(n + m)

@in_out
def summ(x, y):
    """Сумма чисел."""
    print(summ.__doc__)
    res = x + y
    return res

# print(__name__)

if __name__ == '__main__':
    # proba()
    # decor(proba)()
    # etalon(2, 2)
    # res = summ(random.randint(10, 100), random.randint(1, 10)) /.75 + 12.5643736373
    res = summ(random.randint(10, 100), random.randint(1, 10))
    print(res)
    # print(summ(5, 7))
    # def fnc(*args, **kwargs):
    #     print(args)
    #     print(kwargs)



    # fnc(3, 5, 8, x=7, y=10)



    # l = [22, 34, 33, 31, 44, 40, 32]
    # y = 4
    # x = 100 if y > 4 else 10
    # print(x)
    # ls = []
    # for i in l:
    #     if i % 2 == 0:
    #         if i < 35:
    #             ls.append(i)
    #         else:
    #             ls.append(False)
    # ls1 = [i if i < 35 else False for i in l if i % 2 == 0]
    # print(ls)
    # print(ls1)
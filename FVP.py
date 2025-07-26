import math
from functools import reduce

l = [22, 33, 44, 40, 32]
l1 = [2, 3, 44, 5]

# res = list(map(str, l))
# for i in res:
#     print(i, end=' ')
# print(1)
# for i in res:
#     print(i, end=' ')
# print(2)
# def power(n):
#     return n ** 2

# res = list(map(power, l))
# res = map(lambda n: n ** 2, l)
# res = list(map(lambda n, m: n - m, l, l1))
# res = list(map(lambda n, m: n > m, l, l1))
res1 = [n ** 2 for n in l]

# res = list(filter(lambda x: x <= 33, l ))
res1 = [x for x in l if x <= 33]
res1 = (x for x in l if x <= 33)
for i in res1:
    print(i)
print(22222222222)
for i in res1:
    print(i)
# res2 = []
# for x in l:
#     if x <= 33:
#         res2.append(x)
# print(res)
print(res1)
# print(res2)

city = ['У', 'ф', 'а', '-', 4, 5]
# city = list(map(str, city))
# print(''.join(city))

# def agr(n, m):
#     return str(n) + str(m)
# res = reduce(agr, city)
# nums = [2, 3, 4, 5]
# res = reduce(lambda n, m: str(n) + str(m), city)
# res = reduce(lambda n, m: n + m, nums)
# print(sum(nums))
# print(res)

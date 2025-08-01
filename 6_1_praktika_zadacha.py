"""Дан список с названиями фильмов.
Необходимо определить сколько процентов от общего количества
составляют названия с одним, двумя и т.д словами
"""
from асинхронность import *

films = ['Черный пистолет',
         'Варвара краса - длинная коса',
         'Игра в четыре руки',
         'Большие гонки',
         'Коломбо',
         'Танкисты',
         'Бриллиантовая рука'
         ]
print(__name__)
start = time.perf_counter()
asyncio.run(main())
duration = time.perf_counter() - start
print(duration)

#
# dic = {}
#
# for i in films:
#     count_words = len(i.split())
#     # if not count_words in dic:
#     #     dic[count_words] = 1
#     # else:
#     #     dic[count_words] += 1
#     dic[len(i.split())] = dic.get(len(i.split()), 0) + 1
#
# print(dic)
# res1 = sorted(dic.items(), reverse=True)
# print(res1)
# for k, v in res1:
#     percentage = v / len(films)
#     print(f'В {percentage:.2%} фильмов количество слов в названии = {k}')
#
# res2 = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# print(res2)
# for k, v in res2:
#     percentage = v / len(films)
#     print(f'В {percentage:.2%} фильмов количество слов в названии = {k}')

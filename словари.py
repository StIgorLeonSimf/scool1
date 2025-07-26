d = {'Pb': 'Свинец',
     'Au': 'Золото'
     }

# print(list(d))
# print(list(d.keys()))
# print(list(d.values()))
# tpl = list(d.items())
# print(tpl)
# ddd = dict(tpl)
# print(ddd)
# for k in d.keys():
#     print(k, end=' ')
# print()
#
# for v in d.values():
#     print(v, end=' ')
# print()
#
# for k, v in d.items():
#     print(k, v, end='      ')
# print()
#
# x = 7
# ll = [22, 33, 33]
# dd = dict.fromkeys(ll, 12)
# dd[22] = 33
# print(dd)
ls = [i for i in range(1, 11)]
print(ls)
ls = []
for i in range(1, 11):
    ls.append(i)
print(ls)

# dd = {i: i ** 2 for i in range(10, 21)}
dd = {}
for k in range(10, 21):
    dd[k] = k ** 2
print(dd)
s = 'aaaabaaaaanaaaaaaadddaaaanj'
ddd = {}
print(set(s))
for i in set(s):
    ddd[i] = s.count(i)
print(ddd)
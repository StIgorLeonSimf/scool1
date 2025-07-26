"""set"""

# st = set()
st = {22, 33, 44, 55, 99, 88, 88}
# print(st)
# st.add(100)
#
# st.update([1, 2])
#
# n = st.pop()
# try:
#     st.remove(23)
# except KeyError as err:
#     print(f'Нет {err} в множестве ')
# st.discard(100)
#
# print(n)
# print(st)

st1 = {1, 2, 33}
st2 = {1, 2, 44}

# res = st1.union(st2)
# res = st1 | st2

# res = st1.intersection(st2)
# res = st1 & st2

# res = st1.difference(st2)
# res = st2 - st1

# res = st1.symmetric_difference(st2)
res = st1 ^ st2

print(res)
st1 = {1, 2, 33}
st2 = {1, 2, 44}
st3 = {1, 2}

print(st3.issubset(st2))
print(st2.issuperset(st3))
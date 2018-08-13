list_1 = [1, 4, 5, 7, 3, 6, 7, 9]
list_1 = set(list_1)

list_2 = set([2, 6, 0, 66, 22, 8, 4])
# print(list_1, list_2)
# 交集
# print(list_1.intersection(list_2))

# 并集
# print(list_1.union(list_2))

# 差集 in list_1 but not in list_2
# print(list_1.difference(list_2))
# print(list_2.difference(list_1))

# 子集
list_3 = set([1, 3, 7])
# print(list_3.issubset(list_1))
# print(list_1.issuperset(list_3))

# 对称差集
print(list_1.symmetric_difference(list_2))
print("-------------")

# 将两个集合的交集作为一个新集合返回
list_4 = set([5, 6, 7, 8])
print(list_3.isdisjoint(list_4))

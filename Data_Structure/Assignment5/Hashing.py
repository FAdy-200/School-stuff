# from prettytable import PrettyTable as Table
#
# t = Table()
#
#
# def h1(x):
#     x = x ** 2
#     x = str(x)
#     # print(x)
#     x = x[len(x) // 2 - 1:len(x) // 2 + 1]
#     # print(x)
#     return int(x)
#
#
# def h2(x):
#     return int(7 - x % 7)
#
#
# def h(x, i):
#     return int((x + i ** 2) % 100)
#
#
# t.field_names = [i for i in range(0, 100)]
# y = ["-"] * 100
# data = [60, 62, 65, 43, 51]
# dataSquared = [3600, 3844, 4225, 1849, 2601]
# indices = [60, 84, 22, 84, 60]
# # print(dataSquared)
# for i in data:
#     key = h1(i)
#     # print(key)
#     if y[key] == "-":
#         y[key] = i
#     else:
#         c = 1
#         while y[h(key, c)] != "-":
#             c += 1
#         # print(h(key, c))
#         y[h(key, c)] = i
#
# # t.add_row(y)
# # print(t)

x = [i for i in range(100) if i % 2 == 0]


def findPairs(x, n):
    d = dict()
    for i in x:
        d[i] = i
    for i in x:
        # if n - i == i:
        #     continue
        if d.get(n - i):
            yield i, d.get(n - i)


# print(list(findPairs(x, 61)))
def kMost(x, k):
    d = dict()
    z = dict()
    for i in x:
        if d.get(i):
            d[i] += 1
        else:
            d[i] = 1
    for i in x:
        if d[i] == k and z.get(i):
            continue
        elif d[i] == k:
            z[i] = True
            yield x[i]


print(list(kMost([4, 2, 2, 4, 3, 2, 3, 1], 2)))

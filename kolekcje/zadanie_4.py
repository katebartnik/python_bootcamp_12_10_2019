"""
W zadanej liście zamień ze sobą miejscami element największy i
najmniejszy

np. x = [6, 2, 1, 9, 12, 18]
wy:     [6, 2, 18, 9, 12, 1]

min_v = 1
max_v = 18
i_min_v = 2
i_max_v = 5
x[i_min_v]=max_v
x[i_max_v]=min_v

"""

x = [6, 2, 1, 9, 12, 18]

#
# min_v = min(x)
# max_v = max(x)
# i_min_v = x.index(min_v)
# i_max_v = x.index(max_v)
# x[i_min_v]=max_v
# x[i_max_v]=min_v
#
# print(x)

i_min_v = 0
i_max_v = 0

for i,v in enumerate(x):
    if v < x[i_min_v]:
        i_min_v = i
    if v > x[i_max_v]:
        i_max_v = i

# 1.
# temp = x[i_min_v] # wartosc minimalna
# x[i_min_v] = x[i_max_v]  # tu stracilem wartosc min z x
# x[i_max_v] = temp
#
# a, b = 1, 2
# a, b = b, a

x[i_min_v], x[i_max_v] = x[i_max_v], x[i_min_v]

print(x)
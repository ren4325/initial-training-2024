a=[4, 8, 3, 4, 1]
b = [x%2 for x in a ]
print(b)

print(b.count(1))

a=[4, 8, 3, 4, 1]
b = [x for x in a if x%2 == 1]
print(b)

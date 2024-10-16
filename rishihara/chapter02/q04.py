a=[4, 8, 3, 4, 1]
aa = []
for i in a:
    if i % 2 == 0:
        aa.append(0)
    else:
        aa.append(1)
print(aa)

aa.count(1)

a=[4, 8, 3, 4, 1]
b = [x for x in a if x%2 == 1]
print(b)

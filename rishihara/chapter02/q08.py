ls = [x for x in range(2, 101)]
prime = []

for i in ls:
    hantei = True
    for j in prime:
        if i % j == 0:
            hantei = False
            break
    if hantei:
        prime.append(i)

print(prime)
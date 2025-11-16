
x = list((x for x in range(10)))

y = x.copy()

z = y.append(11)

print(x)
print(y)

print(x == y)
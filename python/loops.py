a = 4341
b = 9170
c = 0
for x in range(a, b + 1):
    if x % 2 != 0:
        c += x
print(c)
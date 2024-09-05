d = {}
with open("rosalind_ini6.txt") as file:
    str = file.read()
    for word in str.split(' '):
        x = str.count(word + ' ')
        d[word] = x

for key, value in d.items():
    print(key, value)



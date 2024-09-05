with open('rosalind_rna.txt') as file:
    s = file.read()

t = ''
for i in range(len(s)):
    if (s[i] == 'T'):
        t += 'U'
    else:
        t += s[i]

print(t)
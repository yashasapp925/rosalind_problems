with open('rosalind_revc.txt') as file:
    s = file.read()
t = ''
for i in range((len(s) - 1), -1, -1):
    if (s[i] == 'A'):
        t += 'T'
    elif (s[i] == 'T'):
        t += 'A'
    elif (s[i] == 'G'):
        t += 'C'
    elif (s[i] == 'C'):
        t += 'G'

print(t)
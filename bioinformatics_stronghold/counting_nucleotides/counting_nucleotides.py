with open('rosalind_dna.txt') as file:
    s = file.read()

aCount = 0
tCount = 0
gCount = 0
cCount = 0

for i in range(len(s)):
    if (s[i] == 'A'):
        aCount += 1
    elif (s[i] == 'T'):
        tCount += 1
    elif (s[i] == 'G'):
        gCount += 1
    elif (s[i] == 'C'):
        cCount += 1

print(str(aCount) + ' ' + str(cCount) + ' ' + str(gCount) + ' ' + str(tCount))
file = open("rosalind_ini5.txt", "r")
x = 0
out = open("output.txt", "x")
for line in file:
    if x % 2 == 1:
        out.write(line)
    x += 1
out.close()
file.close()

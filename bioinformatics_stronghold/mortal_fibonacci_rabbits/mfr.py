with open('bioinformatics_stronghold/mortal_fibonacci_rabbits/rosalind_fibd.txt', 'r') as file:
    n, m = map(int, file.readline().split())

rabbits = [1] + [0] * (m - 1)
for i in range(1, n):
    new_pairs = sum(rabbits[1:])
    rabbits = [new_pairs] + rabbits[:-1]
print(sum(rabbits))
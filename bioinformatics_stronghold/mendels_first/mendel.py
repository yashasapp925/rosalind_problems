# k = homozygous dominant
# m = heterozygous
# n = homozygous recessive
with open("bioinformatics_stronghold/mendels_first/rosalind_iprb.txt", "r") as file:
    k, m, n = map(int, file.readline().split())
total = k + m + n

AA = (k / total * (k - 1) / (total - 1) + 0.5 * k / total * m / (total - 1) + 0.5 * m / total * k / (total - 1)
      + 0.25 * m / total * (m - 1) / (total - 1))
Aa = (0.5 * k / total * m / (total - 1) + 0.5 * m / total * k / (total - 1) 
      + k / total * n / (total - 1) + n / total * k / (total - 1) + 0.5 * m / total * n / (total - 1)
      + 0.5 * n / total * m / (total - 1) + 0.5 * m / total * (m - 1) / (total - 1))
print(AA + Aa)
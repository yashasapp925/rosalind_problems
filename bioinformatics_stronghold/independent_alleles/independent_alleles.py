from scipy.stats import binom

with open("bioinformatics_stronghold/independent_alleles/rosalind_lia.txt", "r") as file:
    k, N = map(int, file.readline().split())

total_individuals = 2 ** k
p_AaBb = 1 / 4
prob = 1 - binom.cdf(N - 1, total_individuals, p_AaBb)
print(prob)

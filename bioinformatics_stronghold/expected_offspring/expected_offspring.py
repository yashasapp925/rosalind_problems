with open('bioinformatics_stronghold/expected_offspring/rosalind_iev.txt', 'r') as file:
    couples = list(map(int, file.readline().split()))

total_couples = sum(couples) * 2
probabilities = [1.0, 1.0, 1.0, 0.75, 0.5, 0]
expected_offspring = sum(p * c for p, c in zip(probabilities, couples)) * 2

print(expected_offspring)
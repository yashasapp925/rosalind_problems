with open('bioinformatics_stronghold/dna_motif/rosalind_subs.txt', 'r') as file:
    dna_seq = file.readline().strip()
    motif = file.readline().strip()

locations = []
for i in range(len(dna_seq) - len(motif) + 1):
    if dna_seq[i: i + len(motif)] == motif:
        locations.append(str(i + 1))
print(' '.join(locations))
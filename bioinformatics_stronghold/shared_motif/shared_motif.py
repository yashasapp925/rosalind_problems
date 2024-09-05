sequences = {}
adjacency_list = []

with open('bioinformatics_stronghold/shared_motif/rosalind_lcsm.txt', 'r') as file:
    data = file.read()

sequences = {}
current_id = None
current_sequence = []

for line in data.split('\n'):
    if line.startswith('>'):
        if current_id:
            sequences[current_id] = ''.join(current_sequence)
        current_id = line[1:]
        current_sequence = []
    else:
        current_sequence.append(line.strip())

if current_id:
    sequences[current_id] = ''.join(current_sequence)

dna_seqs = list(sequences.values())
shortest = min(dna_seqs, key=len)
motif = ''
for i in range(len(shortest)):
    for j in range(i + 1, len(shortest) + 1):
        substring = dna_seqs[0][i:j]
        if all(substring in s for s in dna_seqs[1:]):
            if len(substring) > len(motif):
                motif = substring
print(motif)

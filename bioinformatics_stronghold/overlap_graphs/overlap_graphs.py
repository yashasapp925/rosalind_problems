sequences = {}
adjacency_list = []

with open('bioinformatics_stronghold/overlap_graphs/rosalind_grph.txt', 'r') as file:
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

for label1, seq1 in sequences.items():
    for label2, seq2 in sequences.items():
        if label1 != label2 and seq1[-3:] == seq2[:3]:
            adjacency_list.append((label1, label2))

for edge in adjacency_list:
    print(edge[0], edge[1])
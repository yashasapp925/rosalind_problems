sequences = []
with open('bioinformatics_stronghold/consensus_profile/rosalind_cons.txt', 'r') as file:
    sequence = ''
    for line in file:
        if line.startswith('>'):
            if sequence:
                sequences.append(sequence)
                sequence = ''
        else:
            sequence += line.strip()
    if sequence:
        sequences.append(sequence)

profile_matrix = {'A': [], 'C': [], 'G': [], 'T': []}
for i in range(len(sequences[0])):
    column = [s[i] for s in sequences]
    profile_matrix['A'].append(column.count('A'))
    profile_matrix['C'].append(column.count('C'))
    profile_matrix['G'].append(column.count('G'))
    profile_matrix['T'].append(column.count('T'))

consensus = []
for i in range(len(profile_matrix['A'])):
    max_val = float('-inf')
    curr_nuc = ''
    for key in profile_matrix.keys():
        if profile_matrix[key][i] > max_val:
            max_val = profile_matrix[key][i]
            curr_nuc = key
    consensus.append(curr_nuc)
consensus = ''.join(consensus)

print(consensus)
for nucleotide in ['A', 'C', 'G', 'T']:
    print(f"{nucleotide}: {' '.join(map(str, profile_matrix[nucleotide]))}")

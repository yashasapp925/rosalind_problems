file_path = 'bioinformatics_stronghold/hamming_dist/rosalind_hamm.txt'
with open(file_path, 'r') as file:
    first_line = file.readline().strip()
    second_line = file.readline().strip()

seq_1 = first_line
seq_2 = second_line

hamming_dist = 0
for i in range(len(seq_1)):
    pos_1 = seq_1[i]
    pos_2 = seq_2[i]
    if pos_1 != pos_2:
        hamming_dist += 1

print(hamming_dist)
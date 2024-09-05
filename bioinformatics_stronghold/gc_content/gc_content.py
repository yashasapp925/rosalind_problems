file_path = 'rosalind_gc.txt'
with open(file_path, 'r') as file:
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

max_gc_id = None
max_gc_content = -1

for seq_id, sequence in sequences.items():
    gc_count = sequence.count('G') + sequence.count('C')
    total_count = len(sequence)
    gc_content = (gc_count / total_count) * 100 if total_count > 0 else 0
    if gc_content > max_gc_content:
        max_gc_id = seq_id
        max_gc_content = gc_content

print(f'{max_gc_id}\n{max_gc_content:.6f}')
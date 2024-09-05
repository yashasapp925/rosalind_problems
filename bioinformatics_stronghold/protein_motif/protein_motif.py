import requests
import re

def get_fasta(uniprot_id):
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data for {uniprot_id}")
        return None
    fasta_data = response.text
    lines = fasta_data.split('\n')
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>') and line.strip())
    return sequence

ids = []
actual_ids = []
with open('bioinformatics_stronghold/protein_motif/rosalind_mprt.txt', 'r') as in_file:
    for line in in_file:
        ids.append(line.strip()[:6])
        actual_ids.append(line.strip())

motif_regex = re.compile(r'(?=(N[^P][ST][^P]))')
results = {}

i = 0
for id in ids:
    print(f"Fetching data for {id}...")
    sequence = get_fasta(id)
    if sequence:
        print(f"Analyzing sequence for {id}...")
        locations = [m.start(0) + 1 for m in re.finditer(motif_regex, sequence)]
        if locations:
            results[actual_ids[i]] = locations
        else:
            print(f"No motifs found for {id}")
    else:
        print(f"Failed to fetch sequence for {id}")
    i += 1
for uniprot_id, locations in results.items():
    print(uniprot_id)
    print(" ".join(map(str, locations)))

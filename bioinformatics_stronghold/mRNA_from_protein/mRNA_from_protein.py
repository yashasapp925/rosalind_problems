codon_table = {
    'F': ['UUU', 'UUC'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'M': ['AUG'], 
    'V': ['GUU', 'GUC', 'GUA', 'GUG'], 
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'Y': ['UAU', 'UAC'], 
    '*': ['UAA', 'UAG', 'UGA'],
    'H': ['CAU', 'CAC'], 'Q': ['CAA', 'CAG'],
    'N': ['AAU', 'AAC'], 'K': ['AAA', 'AAG'],
    'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'],
    'C': ['UGU', 'UGC'], 'W': ['UGG'], 
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG']
}

with open('bioinformatics_stronghold/mRNA_from_protein/rosalind_mrna.txt') as file:
    protein = file.read()

num_ways = 1

for amino_acid in protein:
    num_ways *= len(codon_table[amino_acid])
    num_ways %= 1000000

num_ways *= len(codon_table['*'])
num_ways %= 1000000

print(num_ways)

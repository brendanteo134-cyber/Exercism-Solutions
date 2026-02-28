def to_rna(dna_strand):
    translations = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = ''
    for letter in dna_strand:
        rna += translations[letter]
    return rna


protein = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine", "UGG": "Tryptophan",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}
def proteins(strand):
    codons = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    ps = []
    for c in codons:
        if protein[c] == "STOP":
            break
        ps.append(protein[c])
    return ps
peptide = input()
peptide_length = len(peptide)
mass_table = {'G': 57,
              'A': 71,
              'S': 87,
              'P': 97,
              'V': 99,
              'T': 101,
              'C': 103,
              'I': 113,
              'L': 113,
              'N': 114,
              'D': 115,
              'K': 128,
              'Q': 128,
              'E': 129,
              'M': 131,
              'H': 137,
              'F': 147,
              'R': 156,
              'Y': 163,
              'W': 186}

cyclospectrum = [0, sum(mass_table[s] for s in peptide)]
peptide += peptide

for length in range(1, peptide_length):
    for position in range(0, peptide_length):
        subpeptide = peptide[position:position + length]
        mass = sum(mass_table[s] for s in subpeptide)
        cyclospectrum.append(mass)

for mass in sorted(cyclospectrum):
    print(str(mass), end=' ')

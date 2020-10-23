spectrum = [int(x) for x in input().split(' ')]
parent_mass = spectrum[-1]

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

names = {'G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'L', 'N', 'D', 'K', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W'}
peptides = [""]
result = []

while len(peptides) != 0:
    # expand:
    peptides_copy = peptides.copy()
    for _ in peptides_copy:
        curr_peptide = peptides.pop(0)
        for name in names:
            is_consistend = True
            mass = 0
            new_peptide = curr_peptide + name
            peptide = new_peptide
            mass = sum(mass_table[c] for c in new_peptide)
            peptide_length = len(new_peptide)
            if mass == parent_mass:
                # cyclospectrum (new_peptide):
                cyclospectrum = [0, mass]
                new_peptide += new_peptide
                for length in range(1, peptide_length):
                    for position in range(0, peptide_length):
                        subpeptide = new_peptide[position:position + length]
                        mass = sum(mass_table[s] for s in subpeptide)
                        cyclospectrum.append(mass)
                cyclospectrum.sort()
                equal = True
                for i, c in enumerate(cyclospectrum):
                    if c != spectrum[i]:
                        equal = False
                        break
                if equal:
                    result.append(peptide)
            else:
                # linear spectrum:
                linear_spectrum = [0, sum(mass_table[s] for s in new_peptide)]
                for length in range(1, peptide_length):
                    position = 0
                    while position + length < peptide_length:
                        subpeptide = new_peptide[position:position + length]
                        mass = sum(mass_table[s] for s in subpeptide)
                        linear_spectrum.append(mass)
                        position += 1
                for val in linear_spectrum:
                    if val not in spectrum:
                        is_consistend = False
                        break
                if is_consistend:
                    peptides.append(new_peptide)

output = []
for i in result:
    seq = [mass_table[p] for p in i]
    if seq not in output:
        output.append(seq)

for out in output:
    for i in range(len(out) - 1):
        print(out[i], end='-')
    print(out[-1], end=' ')
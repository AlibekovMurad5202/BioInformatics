N = int(input())
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
leader_peptid = ("", 0)
leader_board = [leader_peptid]

max_length = int(0.5 + len(spectrum) ** 0.5)

while len(leader_board) != 0:
    if len(leader_board[0][0]) + 1 > max_length:
        break
    # expand:
    leader_board_copy = leader_board.copy()
    for _ in leader_board_copy:
        curr_peptide = leader_board.pop(0)[0]
        for name in names:
            mass_peptide = 0
            new_peptide = curr_peptide + name
            peptide = new_peptide
            mass_peptide = sum(mass_table[c] for c in new_peptide)
            if mass_peptide <= parent_mass:
                # linear score ==================================
                peptide_length = len(new_peptide)
                linear_spectrum = [0, mass_peptide]
                for length in range(1, peptide_length):
                    position = 0
                    while position + length < peptide_length:
                        subpeptide = new_peptide[position:position + length]
                        mass = sum(mass_table[s] for s in subpeptide)
                        linear_spectrum.append(mass)
                        position += 1
                i = j = score_peptide = 0
                linear_spectrum.sort()
                while i < len(linear_spectrum) and j < len(spectrum):
                    if linear_spectrum[i] == spectrum[j]:
                        i += 1
                        j += 1
                        score_peptide += 1
                    else:
                        if linear_spectrum[i] < spectrum[j]:
                            i += 1
                        else:
                            j += 1
                # ===============================================
                leader_board.append((peptide, score_peptide))
                if score_peptide > leader_peptid[1] and mass_peptide == parent_mass:
                    leader_peptid = (peptide, score_peptide)
    leader_board.sort(key=lambda x: x[1], reverse=True)
    if len(leader_board) > N:
        threshold = leader_board[N - 1][1]
        leader_board = [x for x in leader_board if x[1] >= threshold]
            
output = [mass_table[i] for i in leader_peptid[0]]
for i in range(len(output) - 1):
    print(output[i], end='-')
print(output[-1], end='')
text = input()
dna = text
peptide = input()
peptide_length = len(peptide) * 3
dna_length = len(text)

complement_dict = {'A': 'T',
                   'T': 'A',
                   'C': 'G',
                   'G': 'C'}

rna_codon_table = {'AAA': 'K',
                   'AAC': 'N',
                   'AAG': 'K',
                   'AAU': 'N',
                   'ACA': 'T',
                   'ACC': 'T',
                   'ACG': 'T',
                   'ACU': 'T',
                   'AGA': 'R',
                   'AGC': 'S',
                   'AGG': 'R',
                   'AGU': 'S',
                   'AUA': 'I',
                   'AUC': 'I',
                   'AUG': 'M',
                   'AUU': 'I',
                   'CAA': 'Q',
                   'CAC': 'H',
                   'CAG': 'Q',
                   'CAU': 'H',
                   'CCA': 'P',
                   'CCC': 'P',
                   'CCG': 'P',
                   'CCU': 'P',
                   'CGA': 'R',
                   'CGC': 'R',
                   'CGG': 'R',
                   'CGU': 'R',
                   'CUA': 'L',
                   'CUC': 'L',
                   'CUG': 'L',
                   'CUU': 'L',
                   'GAA': 'E',
                   'GAC': 'D',
                   'GAG': 'E',
                   'GAU': 'D',
                   'GCA': 'A',
                   'GCC': 'A',
                   'GCG': 'A',
                   'GCU': 'A',
                   'GGA': 'G',
                   'GGC': 'G',
                   'GGG': 'G',
                   'GGU': 'G',
                   'GUA': 'V',
                   'GUC': 'V',
                   'GUG': 'V',
                   'GUU': 'V',
                   'UAA': '',
                   'UAC': 'Y',
                   'UAG': '',
                   'UAU': 'Y',
                   'UCA': 'S',
                   'UCC': 'S',
                   'UCG': 'S',
                   'UCU': 'S',
                   'UGA': '',
                   'UGC': 'C',
                   'UGG': 'W',
                   'UGU': 'C',
                   'UUA': 'L',
                   'UUC': 'F',
                   'UUG': 'L',
                   'UUU': 'F'}

for i in range(0, dna_length - peptide_length + 1):
    for substring in [text[i:i + peptide_length]]:
        reverse_complement = "".join([complement_dict[s] for s in substring][::-1])
        substring_translation = ""
        substring_rc_translation = ""
        for j in range(0, len(substring), 3):
            substring_translation += rna_codon_table[substring[j:j + 3].replace('T', 'U')]
            substring_rc_translation += rna_codon_table[reverse_complement[j:j + 3].replace('T', 'U')]
        if peptide in (substring_translation, substring_rc_translation):
            print(substring)

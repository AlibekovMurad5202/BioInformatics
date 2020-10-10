reversed_pattern = input()[::-1]
complement_dict = {'A': 'T',
                   'T': 'A',
                   'C': 'G',
                   'G': 'C'}
reverse_complement = "".join([complement_dict[i] for i in reversed_pattern])
print(reverse_complement)

def motif_enumeration(DNA, k, d):
    patterns = set()
    for dna in DNA:
        for i in range(len(dna) - k):
            for pattern in mutated_patterns(dna[i:i + k], k, d):
                if check_pattern(DNA, pattern, k, d):
                    patterns.add(pattern)
    return patterns


def check_pattern(DNA, pattern, k, d) -> bool:
    for dna in DNA:
        hamming_distances = []
        for j in range(len(dna) - k + 1):
            pattern_iter = dna[j:j + k]
            hamming_distances.append(sum(not c_1 == c_2 for c_1, c_2 in zip(pattern, pattern_iter)))
        if min(hamming_distances) > d:
            return False
    return True


def mutated_patterns(pattern, k, d) -> set:
    patterns = set([pattern])
    for _ in range(d):
        new_patterns = list(patterns)
        while len(new_patterns) != 0:
            new_pattern = new_patterns.pop()
            for i in range(k):
                for c in ["A", "C", "G", "T"]:
                    patterns.add(new_pattern[:i] + c + new_pattern[i + 1:k])
    return patterns


if __name__ == "__main__":
    k, d = map(int, input().split(' '))
    DNA = [input() for _ in range(4)]
    print(" ".join(list(motif_enumeration(DNA, int(k), int(d)))))

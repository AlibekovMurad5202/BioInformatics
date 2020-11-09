def median_string(DNA, k):
    median = ""
    result_distance = -1
    for pattern in all_patterns(k):
        pattern_distance = distance(DNA, pattern)
        if result_distance > pattern_distance or result_distance == -1:
            result_distance = pattern_distance
            median = pattern
    return median


def distance(DNA, pattern):
    distances = []
    for dna in DNA:
        hamming_distances = []
        for j in range(len(dna) - k + 1):
            pattern_iter = dna[j:j + k]
            hamming_distances.append(sum(not c_1 == c_2 for c_1, c_2 in zip(pattern, pattern_iter)))
        distances.append(min(hamming_distances))
    return sum(distances)


def all_patterns(k) -> list:
    patterns = [""]
    while len(patterns[0]) < k:
        new_pattern = patterns.pop(0)
        for c in ["A", "C", "G", "T"]:
            patterns.append(new_pattern + c)
    return patterns


if __name__ == "__main__":
    k = int(input())
    DNA = [input() for _ in range(10)]
    print(median_string(DNA, k))

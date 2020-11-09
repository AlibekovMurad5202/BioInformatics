def greedy_motif_search(DNA, k, t):
    best_motifs = [dna[:k] for dna in DNA]
    for j in range(len(DNA[0]) - k + 1):
        motifs = [DNA[0][j:j + k]]
        for i in range(1, t):
            profile = form_profile(motifs, k)
            motifs.append(profile_most_probable_k_mer(DNA[i], k, profile))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


def form_profile(motifs, k) -> dict:
    t = len(motifs)
    profile = { 'A': [0] * k, 'C': [0] * k, 'G': [0] * k, 'T': [0] * k }
    for motif in motifs:
        for i in range(k):
            profile[motif[i]][i] += 1. / t
    return { c: profile[c] for c in ('A', 'C', 'G', 'T') }


def profile_most_probable_k_mer(dna, k, profile):
    probs = []
    for i in range(len(dna) - k + 1):
        prob_i = 1.
        for j in range(k):
            prob_i *= profile[dna[i + j]][j]
        probs.append((prob_i, i))
    max_idx = max(probs, key=lambda prob: prob[0])[1]
    return dna[max_idx:max_idx + k]


def score(motifs) -> int:
    return sum(hamming_distance(consensus(motifs), motif) for motif in motifs)


def consensus(motifs):
    consensus_motif = ""
    k = len(motifs[0])
    profile = form_profile(motifs, k)
    for i in range(k):
        probs = [(profile[c][i], c) for c in ('A', 'C', 'G', 'T')]
        consensus_motif += max(probs, key=lambda prob: prob[0])[1]
    return consensus_motif


def hamming_distance(motif_1, motif_2) -> int:
    h_dist = 0
    for c_1, c_2 in zip(motif_1, motif_2):
        h_dist += 0 if c_1 == c_2 else 1
    return h_dist


if __name__ == "__main__":
    k, t = input().split(' ')
    k, t = int(k), int(t)
    DNA = [input() for _ in range(t)]
    motifs = greedy_motif_search(DNA, k, t)
    for motif in motifs:
        print(motif)
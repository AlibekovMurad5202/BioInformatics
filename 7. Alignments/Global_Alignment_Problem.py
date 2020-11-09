def BLOSUM_62() -> dict:
    return [
        [ 4,  0, -2, -1, -2,  0, -2, -1, -1, -1, -1, -2, -1, -1, -1,  1,  0,  0, -3, -2],
        [ 0,  9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
        [-2, -3,  6,  2, -3, -1, -1, -3, -1, -4, -3,  1, -1,  0, -2,  0, -1, -3, -4, -3],
        [-1, -4,  2,  5, -3, -2,  0, -3,  1, -3, -2,  0, -1,  2,  0,  0, -1, -2, -3, -2],
        [-2, -2, -3, -3,  6, -3, -1,  0, -3,  0,  0, -3, -4, -3, -3, -2, -2, -1,  1,  3],
        [ 0, -3, -1, -2, -3,  6, -2, -4, -2, -4, -3,  0, -2, -2, -2,  0, -2, -3, -2, -3],
        [-2, -3, -1,  0, -1, -2,  8, -3, -1, -3, -2,  1, -2,  0,  0, -1, -2, -3, -2,  2],
        [-1, -1, -3, -3,  0, -4, -3,  4, -3,  2,  1, -3, -3, -3, -3, -2, -1,  3, -3, -1],
        [-1, -3, -1,  1, -3, -2, -1, -3,  5, -2, -1,  0, -1,  1,  2,  0, -1, -2, -3, -2],
        [-1, -1, -4, -3,  0, -4, -3,  2, -2,  4,  2, -3, -3, -2, -2, -2, -1,  1, -2, -1],
        [-1, -1, -3, -2,  0, -3, -2,  1, -1,  2,  5, -2, -2,  0, -1, -1, -1,  1, -1, -1],
        [-2, -3,  1,  0, -3,  0,  1, -3,  0, -3, -2,  6, -2,  0,  0,  1,  0, -3, -4, -2],
        [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2,  7, -1, -2, -1, -1, -2, -4, -3],
        [-1, -3,  0,  2, -3, -2,  0, -3,  1, -2,  0,  0, -1,  5,  1,  0, -1, -2, -2, -1],
        [-1, -3, -2,  0, -3, -2,  0, -3,  2, -2, -1,  0, -2,  1,  5, -1, -1, -3, -3, -2],
        [ 1, -1,  0,  0, -2,  0, -1, -2,  0, -2, -1,  1, -1,  0, -1,  4,  1, -2, -3, -2],
        [ 0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1,  0, -1, -1, -1,  1,  5,  0, -2, -2],
        [ 0, -1, -3, -2, -1, -3, -3,  3, -2,  1,  1, -3, -2, -2, -3, -2,  0,  4, -3, -1],
        [-3, -2, -4, -3,  1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11,  2],
        [-2, -2, -3, -2,  3, -3,  2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1,  2,  7]
    ]


def idx(c) -> int:
    indexes = {
        '-':  0, 'A':  1, 'C':  2, 'D':  3, 'E':  4, 'F':  5, 'G':  6, 
        'H':  7, 'I':  8, 'K':  9, 'L': 10, 'M': 11, 'N': 12, 'P': 13, 
        'Q': 14, 'R': 15, 'S': 16, 'T': 17, 'V': 18, 'W': 19, 'Y': 20 
    }
    return indexes[c]


def global_alignment_backtrack(v, w, sigma, score) -> dict:
    n, m = len(v), len(w)
    s = [[0] * (m + 1) for _ in range(n + 1)]
    backtrack = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] - sigma
        backtrack[i][0] = 1
    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] - sigma
        backtrack[0][j] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(
                s[i - 1][j] - sigma,
                s[i][j - 1] - sigma,
                s[i - 1][j - 1] + score[idx(v[i - 1]) - 1][idx(w[j - 1]) - 1]
            )
            if s[i][j] == s[i - 1][j] - sigma:
                backtrack[i][j] = 1
            elif s[i][j] == s[i][j - 1] - sigma:
                backtrack[i][j] = 0
            else:
                backtrack[i][j] = -1
    return backtrack, s[n][m]


def global_alignment(backtrack, s, t, result, i, j):
    if i == 0 and j == 0:
        return result
    if backtrack[i][j] == 1:
        result[0] += s[i - 1]
        result[1] += '-'
        global_alignment(backtrack, s, t, result, i - 1, j)
    elif backtrack[i][j] == 0:
        result[0] += '-'
        result[1] += t[j - 1]
        global_alignment(backtrack, s, t, result, i, j - 1)
    else:
        result[0] += s[i - 1]
        result[1] += t[j - 1]
        global_alignment(backtrack, s, t, result, i - 1, j - 1)
    return result


if __name__ == "__main__":
    s = input()
    t = input()
    sigma = 5
    backtrack, max_score = global_alignment_backtrack(s, t, sigma, BLOSUM_62())
    result = global_alignment(backtrack, s, t, ["", ""], len(s), len(t))
    print(max_score)
    print(result[0][::-1])
    print(result[1][::-1])

def LCS_backtrack(v, w):
    n, m = len(v), len(w)
    s = [[0] * (m + 1) for _ in range(n + 1)]
    backtrack = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j], s[i][j - 1], (s[i - 1][j - 1] + 1) * (v[i - 1] == w[j - 1]))
            if s[i][j] == s[i - 1][j]:
                backtrack[i][j] = 1
            elif s[i][j] == s[i][j - 1]:
                backtrack[i][j] = 0
            else:
                backtrack[i][j] = -1
    return backtrack    


def output_LCS(backtrack, s, i, j) -> None:
    if i == 0 or j == 0:
        return
    if backtrack[i][j] == 1:
        output_LCS(backtrack, s, i - 1, j)
    elif backtrack[i][j] == 0:
        output_LCS(backtrack, s, i, j - 1)
    else:
        output_LCS(backtrack, s, i - 1, j - 1)
        print(s[i - 1], end='')


if __name__ == "__main__":
    s = input()
    t = input()
    backtrack = LCS_backtrack(s, t)
    output_LCS(backtrack, s, len(s), len(t))

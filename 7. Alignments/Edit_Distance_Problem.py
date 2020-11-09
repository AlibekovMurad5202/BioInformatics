v = input()
w = input()
n, m = len(v), len(w)
s = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    s[i][0] = s[i - 1][0] + 1

for j in range(1, m + 1):
    s[0][j] = s[0][j - 1] + 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = min(
            s[i - 1][j] + 1,
            s[i][j - 1] + 1,
            s[i - 1][j - 1] if v[i - 2] == w[j - 2] else s[i - 1][j - 1] + 1
        )

edit_distance = s[n][m]
print(edit_distance)

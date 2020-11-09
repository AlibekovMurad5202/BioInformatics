n, m = input().split(' ')
n, m = int(n), int(m)

down = [[int(x) for x in input().split(' ')] for _ in range(n)]
_ = input()
right = [[int(x) for x in input().split(' ')] for _ in range(n + 1)]

s = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    s[i][0] = s[i - 1][0] + down[i - 1][0]

for j in range(1, m + 1):
    s[0][j] = s[0][j - 1] + right[0][j - 1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])

print(s[n][m])

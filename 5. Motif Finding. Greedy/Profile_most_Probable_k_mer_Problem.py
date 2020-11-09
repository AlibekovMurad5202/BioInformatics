text = input()
k = int(input())
profile_A = [float(x) for x in input().split(' ')]
profile_C = [float(x) for x in input().split(' ')]
profile_G = [float(x) for x in input().split(' ')]
profile_T = [float(x) for x in input().split(' ')]
profile = { 'A': profile_A, 'C': profile_C, 'G': profile_G, 'T': profile_T }

probs = []
for i in range(len(text) - k + 1):
    prob_i = 1.
    for j in range(k):
        prob_i *= profile[text[i + j]][j]
    probs.append((prob_i, i))
max_idx = max(probs, key=lambda prob: prob[0])[1]
print(text[max_idx:max_idx + k])

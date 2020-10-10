text = input()
k = int(input())
length = len(text)
frequent_patterns = set()
count = [0] * length

for i in range(0, length - k):
    pattern = text[i:i + k]
    for j in range(0, length - k):
        if text[j:j + k] == pattern:
            count[i] += 1
max_count = max(count)

for i in range(0, length - k):
    if count[i] == max_count:
        frequent_patterns.add(text[i:i + k])

for pattern in frequent_patterns:
    print(pattern, end=' ')
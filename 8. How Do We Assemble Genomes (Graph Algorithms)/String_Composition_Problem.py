k = int(input())
text = input()

length = len(text) - k + 1
reads = sorted(text[i:i + k] for i in range(0, length))
for read in reads:
    print(read)

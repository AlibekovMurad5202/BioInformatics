pattern = input()
genome = input()

count = 0
for i in range(0, len(genome) - len(pattern) - 1):
    if genome[i:i + len(pattern)] == pattern:
        count += 1
        
print(count)

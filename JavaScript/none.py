import sys

n = 5
segments = [(1, 3), (2, 4), (5, 8), (6, 9), (7, 10)]

max_point = 0
for elem in segments:
    max_point = max(elem[1], max_point)

count = [0] * (max_point + 1)
min_of_max_count = sys.maxsize

for i in range(1, n+1):
    for j, elem in enumerate(segments, start=1):
        if i == j:
            continue

        start, end = elem[0], elem[1]

        for k in range(start, end+1):
            count[k] += 1
        
    max_count = max(count)
    min_of_max_count = min(max_count, min_of_max_count)
    print(max_count)

print(min_of_max_count)
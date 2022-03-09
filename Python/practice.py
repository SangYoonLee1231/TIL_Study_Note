x, y, w, h = tuple(map(int, input().split()))
dist = [x, y, (h - y), (w - x)]

min = 1000
for elem in dist:
  if elem < min:
    min = elem

print(min)
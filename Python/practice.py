d = {
  'cs101' : 'python programming',
  'cs202' : 'data structures'
}

print(d.get('cs101'))
print(d.get('cs102', 0))
print(d.items())
print(d.keys())
print(d.values())


s = [
  int(x)
  for x in input().split()
]

print(s)
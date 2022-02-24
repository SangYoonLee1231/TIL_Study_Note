n = int(input())
lst = list(map(int, input().split()))
leader_ablity, member_ablity = tuple(map(int, input().split()))

ans = 0

for i, elem in enumerate(lst):
    lst[i] -= leader_ablity
    ans += 1

for i, elem in enumerate(lst):
    while lst[i] > 0:
        lst[i] -= member_ablity
        ans += 1
    
print(ans)
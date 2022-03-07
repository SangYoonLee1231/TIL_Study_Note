n = int(input())
lst = list(map(int, input().split()))

if n == 1:
    print(lst[0] * lst[0])
else:
    print(max(lst) * min(lst))

# 약수가 1개이면 그 값을 제곱
# 약수가 2개 이상이면 제일 큰 값 * 제일 작은 값

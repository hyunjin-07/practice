# problem: 10871
# tier: bronze

# N, X 입력
N, X = map(int, input().split())

# 수열 입력
arr = list(map(int, input().split()))

# X보다 작은 수만 출력
for i in arr:
    if i < X:
        print(i, end=" ")
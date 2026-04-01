# problem: 10871
# tier: bronze

# N과 X 입력
N, X = map(int, input().split())

# 정수 리스트 입력
arr = list(map(int, input().split()))

# X보다 작은 수 출력
for i in arr:
    if i < X:
        print(i, end=" ")
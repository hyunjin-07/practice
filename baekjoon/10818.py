# problem: 10818
# tier: bronze

# 정수 개수 입력
N = int(input())

# 정수 리스트 입력
arr = list(map(int, input().split()))

# 최소값과 최대값 출력
print(min(arr), max(arr))
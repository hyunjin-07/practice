# problem: 10807
# tier: bronze

# 정수 개수 입력
N = int(input())

# 정수 리스트 입력
arr = list(map(int, input().split()))

# 찾을 값 입력
V = int(input())

# 리스트에서 V의 개수 출력
print(arr.count(V))
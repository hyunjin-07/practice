# problem: 10807
# tier: bronze

# 정수의 개수 N 입력
N = int(input())

# 공백으로 구분된 정수들을 리스트로 저장
arr = list(map(int, input().split()))

# 개수를 찾으려는 정수 V 입력
V = int(input())

# 리스트 내 정수 V의 출현 횟수 계산 및 출력
print(arr.count(V))
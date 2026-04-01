# problem: 2525
# tier: bronze

H, M = map(int, input().split())
M2 = int(input())

# 1. 분 더하기
M += M2

# 2. 넘친 시간을 시에 더하기
H += M // 60

# 3. 분은 60으로 나눈 나머지
M = M % 60

# 4. 시는 24시간 기준으로 맞추기
H = H % 24

print(H, M) 
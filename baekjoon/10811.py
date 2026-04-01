# problem: 10811
# tier: bronze

# 바구니 수 N, 역순 수행 횟수 M 입력
N, M = map(int, input().split())

# 1~N 번호 바구니 초기화
arr = list(range(1, N+1))

# M번 구간 역순
for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1:j] = arr[i-1:j][::-1]

# 결과 출력
print(*arr)
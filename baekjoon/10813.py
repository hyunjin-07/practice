# problem: 10813
# tier: bronze

# 바구니 수 N, 교환 횟수 M 입력
N, M = map(int, input().split())

# 바구니 배열 초기화
arr = [0] * N

# 1~N 번호 채우기
for i in range(N):
    arr[i] = i + 1

# M번 교환
for _ in range(M):
    # 교환할 바구니 번호 입력
    i, j = map(int, input().split())
    # 값 교환
    arr[i-1], arr[j-1] = arr[j-1], arr[i-1]

# 결과 출력
print(*arr)
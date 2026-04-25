# problem: 2566
# tier: bronze

max_val = -1
max_row = 0
max_col = 0

# 9x9 격자판 입력 처리
for i in range(9):
    row = list(map(int, input().split()))
    for j in range(9):
        # 현재 값이 저장된 최댓값보다 크거나 같으면 갱신
        # (모든 값이 0일 경우를 대비해 -1로 초기화하거나 >= 사용)
        if row[j] > max_val:
            max_val = row[j]
            max_row = i + 1
            max_col = j + 1

# 최댓값 출력
print(max_val)
# 최댓값이 위치한 행, 열 출력
print(max_row, max_col)
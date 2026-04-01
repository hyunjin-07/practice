# problem: 2562
# tier: bronze

# 입력 받을 9개의 수를 리스트에 저장
arr = []
for i in range(9):
    num = int(input())
    arr.append(num)

# 최댓값과 인덱스 초기화
max_val = arr[0]
max_idx = 0

# 리스트를 순회하며 최댓값과 위치 찾기
for i in range(9):
    if arr[i] > max_val:
        max_val = arr[i]
        max_idx = i

# 최댓값과 위치(1-index) 출력
print(max_val)
print(max_idx + 1)
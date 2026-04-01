# problem: 5597
# tier: bronze

# 출석 배열 초기화 (1~30번)
arr = [0] * 31

# 제출한 학생 번호 표시
for _ in range(28):
    num = int(input())
    arr[num] = 1

# 제출하지 않은 학생 출력
for i in range(1, 31):
    if arr[i] == 0:
        print(i)
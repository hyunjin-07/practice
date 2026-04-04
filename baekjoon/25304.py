# problem: 25304
# tier: bronze

# 총 금액과 물건 종류 수 입력
total = int(input())
N = int(input())
total1 = 0

# 물건별 가격과 개수 입력받아 합계 계산
for i in range(N):
    A, B = map(int, input().split())
    total1 = total1 + (A * B)

# 계산된 합계와 총 금액 비교 및 결과 출력
if total == total1:
    print("Yes")
else:
    print("No")
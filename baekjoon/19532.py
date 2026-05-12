# problem: 19532
# tier: bronze

# 정수 a, b, c, d, e, f를 입력받음
# 연립방정식 형태: ax + by = c / dx + ey = f
a, b, c, d, e, f = map(int, input().split())

# x와 y의 범위가 -999부터 999까지로 제한되어 있으므로
# 모든 정수 쌍을 대입해보는 브루트 포스(Brute Force) 방식 사용
found = False
for x in range(-999, 1000):
    for y in range(-999, 1000):
        # 주어진 두 방정식을 모두 만족하는 (x, y) 좌표 찾기
        if (a * x + b * y == c) and (d * x + e * y == f):
            print(x, y)
            found = True
            break  # y 루프 탈출
    if found:
        break      # x 루프 탈출
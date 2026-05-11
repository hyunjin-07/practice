# problem: 24313
# tier: silver

# f(n) = a1*n + a0
a1, a0 = map(int, input().split())
# c: 상수, n0: n의 최솟값
c = int(input())
n0 = int(input())

# Big-O 정의: 모든 n >= n0에 대하여 f(n) <= c * g(n)
# 여기서는 g(n) = n 이므로, a1*n + a0 <= c*n 이 성립해야 함
# 1. n0를 대입했을 때 성립하는가? (a1*n0 + a0 <= c*n0)
# 2. 기울기 조건: n이 무한히 커질 때도 성립하려면 c >= a1 이어야 함

if (a1 * n0 + a0 <= c * n0) and (c >= a1):
    print(1)
else:
    print(0)
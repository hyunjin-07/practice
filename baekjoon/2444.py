# problem: 2444
# tier: bronze

# 기준 값(n) 입력
n = int(input())

# 위쪽 피라미드 (1층부터 n층까지)
for i in range(1, n + 1):
    # 공백: (n - i)개, 별: (2*i - 1)개
    print(" " * (n - i) + "*" * (2 * i - 1))

# 아래쪽 역피라미드 (n-1층부터 1층까지)
for i in range(n - 1, 0, -1):
    # 공백: (n - i)개, 별: (2*i - 1)개
    print(" " * (n - i) + "*" * (2 * i - 1))
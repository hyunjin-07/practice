# Problem: 2444
# Tier: Bronz

n = int(input())  # 줄 개수 입력

# 위쪽 피라미드
for i in range(1, n + 1):
    # 공백: (n - i)개
    print(" " * (n - i), end="")
    # 별: (2*i - 1)개
    print("*" * (2 * i - 1))

# 아래쪽 역피라미드
for i in range(n - 1, 0, -1):
    # 공백: (n - i)개
    print(" " * (n - i), end="")
    # 별: (2*i - 1)개
    print("*" * (2 * i - 1))
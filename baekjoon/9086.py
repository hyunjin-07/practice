# problem: 9086
# tier: bronze

# 테스트 케이스 수 T 입력
T = int(input())

# 각 문자열 처리
for _ in range(T):
    # 문자열 입력
    s = input()
    # 첫 글자와 마지막 글자 출력
    print(s[0] + s[-1])
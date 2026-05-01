# problem: 10988
# tier: bronze

# 단어 입력
word = input()

# 뒤집은 단어와 원래 단어 비교 (슬라이싱 사용)
if word == word[::-1]:
    # 팰린드롬인 경우 1 출력
    print(1)
else:
    # 아닌 경우 0 출력
    print(0)
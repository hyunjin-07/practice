# problem: 10809
# tier: bronze

# 단어 S 입력
S = input()

# 알파벳 a부터 z까지 순회 (ASCII 97~122)
for i in range(ord('a'), ord('z') + 1):
    # 각 알파벳이 S에 처음 나타나는 인덱스 출력, 없으면 -1
    print(S.find(chr(i)), end=' ')
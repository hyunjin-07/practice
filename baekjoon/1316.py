# problem: 1316
# tier: silver

# 단어의 개수 N 입력
N = int(input())
group_word_cnt = N

for _ in range(N):
    word = input()
    for i in range(len(word) - 1):
        # 현재 문자와 다음 문자가 다를 때 (연속이 끊겼을 때)
        if word[i] != word[i+1]:
            # 이후에 현재 문자가 다시 등장한다면 그룹 단어가 아님
            if word[i] in word[i+1:]:
                group_word_cnt -= 1
                break

# 그룹 단어의 개수 출력
print(group_word_cnt)
# problem: 25305
# tier: bronze

# 응시자의 수 N과 상을 받는 사람의 수 k 입력
n, k = map(int, input().split())

# 각 응시자의 점수 리스트 입력
scores = list(map(int, input().split()))

# 점수를 내림차순(큰 순서대로) 정렬
scores.sort(reverse=True)

# 상을 받는 커트라인은 정렬된 리스트에서 k번째 점수임
# 인덱스는 0부터 시작하므로 k-1번째 값을 출력
print(scores[k-1])
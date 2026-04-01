H, M = map(int, input().split())
M2 = int(input())

#분 더하기
M = M + M2
#넘친 분 시간에 추가
H = H + (M // 60)
#시간에 추가하고 남은 분
M = M % 60
#24시가 되면 0시로
H = H % 24
print(H, M) 
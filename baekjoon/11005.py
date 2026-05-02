# problem: 11005
# tier: bronze

# 10진법 수 N과 변환할 진법 B 입력
N, B = map(int, input().split())

# 변환 시 사용할 숫자 및 알파벳 정의
# 0-9는 그대로, 10부터는 A, B, C... 순서로 매핑
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ''

# N이 0이 될 때까지 B로 나누며 나머지 기록
while N != 0:
    # 나머지에 해당하는 문자를 결과 앞에 추가
    result += str(tmp[N % B])
    # N을 B로 나눈 몫으로 갱신
    N //= B

# 역순으로 계산되었으므로 뒤집어서 출력
print(result[::-1])
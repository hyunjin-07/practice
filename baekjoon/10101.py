# problem: 10101
# tier: bronze

# 세 각 입력
a = int(input())
b = int(input())
c = int(input())

# 세 각의 합이 180이 아닌 경우
if a + b + c != 180:
    print("Error")
# 세 각이 모두 60인 경우
elif a == b == c == 60:
    print("Equilateral")
# 두 각만 같은 경우
elif a == b or b == c or a == c:
    print("Isosceles")
# 세 각이 모두 다른 경우
else:
    print("Scalene")
# problem: 25304
# tier: bronze

total = int(input())
N = int(input())
total1 = 0

for i in range(N):
    A, B = map(int, input().split())
    total1 = total1 + (A * B)

if total == total1:
    print("Yes")
else:
    print("No")
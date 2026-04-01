# 정수의 갯수를 N에 대입
N = int(input())
# 입력한 정수들을 리스트에 넣고 arr에 대입
arr = list(map(int, input().split()))
# 찾으려고 하는 정수를 v에 대입
v = int(input())

print(arr.count(v)) 
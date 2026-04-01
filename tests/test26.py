arr = []

for i in range(9):
    num = int(input())
    arr.append(num)

max_v = arr[0]
max_i = 0

for i in range(9): 
    if arr[i] > max_v:
        max_v = arr[i]
        max_i = i

print(max_v, max_i + 1)
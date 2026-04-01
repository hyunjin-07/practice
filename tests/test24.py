N = int(input())
arr = list(map(int, input().split()))
number1 = arr[0]
number2 = arr[0]

for i in arr:
    if i > number1:
        number1 = i
    if i < number2:
        number2 = i 
        
print(number2, number1)
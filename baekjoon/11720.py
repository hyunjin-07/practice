# problem: 11720
# tier: bronze

# 숫자의 개수 입력
n = int(input()) 
# 공백 없는 숫자 문자열 입력
nums = input()            

total = 0

# 문자열의 각 문자를 정수로 변환하여 합산
for num in nums:
    total += int(num)    

# 최종 합계 출력
print(total)
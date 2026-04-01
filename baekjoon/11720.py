# problem: 11720
# tier: bronze

# 숫자의 개수
n = int(input()) 
# 숫자 문자열 입력        
nums = input()            

total = 0

# 한 자리씩 더하기
for num in nums:
    total += int(num)    

 # 결과 출력
print(total)     
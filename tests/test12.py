def add_all(*args):
    # args가 어떻게 들어오는지 출력해볼게요
    print(f"들어온 값: {args}") 
    print(f"데이터 타입: {type(args)}")
    
    # 튜플이니까 반복문으로 돌리거나 합을 구할 수 있어요
    return sum(args)

# 사용해보기
result = add_all(1, 2, 3, 4, 5)
print(f"결과: {result}") 
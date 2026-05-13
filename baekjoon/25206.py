# problem: 25206
# tier: silver

# 학점별 평점 딕셔너리
grade_points = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0
}

total_score = 0  # (학점 * 평점)의 합계
total_credits = 0  # 총 학점 이수 합계

# 20줄에 걸쳐 입력 처리
for _ in range(20):
    data = input().split()
    if not data: break
    
    subject, credit, grade = data
    credit = float(credit)

    # 등급이 P인 과목은 계산에서 제외
    if grade != "P":
        total_score += credit * grade_points[grade]
        total_credits += credit

# 전공평점 = (학점 * 평점)의 합 / 학점 총합
# total_credits가 0인 경우 예외 처리는 문제 조건상 생략 가능 (최소 1과목 수강)
print(f"{total_score / total_credits:.6f}")
# problem: 24267
# tier: bronze

# MenOfPassion(A, n) {
#     sum <- 0;
#     for i from 1 to n - 2
#         for j from i + 1 to n - 1
#             for k from j + 1 to n
#                 sum <- sum + A[i] * A[j] * A[k]; # 코드1
#     return sum;
# }

n = int(input())

# i, j, k는 서로 다른 3개의 수를 n개 중에서 순서 상관없이 뽑는 조합과 같음
# nC3 = (n * (n - 1) * (n - 2)) / (3 * 2 * 1)
print(n * (n - 1) * (n - 2) // 6)
# n^3에 비례하므로 최고차항의 차수는 3
print(3)
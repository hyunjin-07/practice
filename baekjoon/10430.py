# problem: 10430
# tier: bronze

A, B, C, = map(int, input().split())
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)
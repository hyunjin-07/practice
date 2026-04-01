# problem: 2884
# tier: bronze

H, M = map(int, (input().split()))

#45분보다 크거나 같으면 -45분
if M >= 45:
    M = M - 45
#45분보다 작으면  
else:
    #1시간을 빼고
    if H == 0:
        H = 23
    else:
        H = H - 1
    #15분을 더함
    M = M + 15

print(H, M)
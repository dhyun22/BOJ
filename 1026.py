# 1. B리스트 건드려서 답만 도출하기
# 2. B리스트 안건들고 pop 이용

N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
S = 0

# X = sorted(A)
# Y = sorted(B, reverse=True)

for i in range(N):
    X = min(A)
    Y = max(B)
    S += X*Y
    A.pop(A.index(X))
    B.pop(B.index(Y))

print(S)

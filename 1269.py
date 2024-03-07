# 리스트를 사용할 경우 시간 복잡도  = O(N*M)
# 집합을 사용할 경우 시간 복잡도 = O(M)

N, M = map(int, input().split(' '))
# A = []
# B = []
# result = []
# A = list(map(int, input().split(' ')))
# B = list(map(int, input().split(' ')))
# list 접근은 복잡도 높아짐 -> set 사용

A = set(map(int, input().split(' ')))
B = set(map(int, input().split(' ')))
result = len(A-B) + len(B-A)
print(result)

# in 연산자의 시간복잡도
# list, tuple = O(n)
# set, dictionary = O(1)

N, M = map(int, input().split(' '))
nothear = []
notseen = []
result = []
for i in range(N):
    nothear.append(input())
for j in range(M):
    notseen.append(input())
result = list(set(nothear) & set(notseen))
result.sort()
print(len(result))
for l in result:
    print(l)

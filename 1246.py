N, M = map(int, input().split(' '))
p = []
result = 0
price = 0
for m in range(M):
    p.append(int(input()))
p.sort(reverse=True)
for i in range(min(N, M)):
    if result <= (i+1)*p[i]:
        price = p[i]
        result = (i+1)*p[i]

print(price, result)

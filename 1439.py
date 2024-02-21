N = str(input())
k = len(N)
cnt = 0
i = 0
while i < k-1:
    if N[i] != N[i+1]:
        cnt += 1
        i += 1
    else:
        i += 1
if cnt % 2 == 0:
    result = cnt//2
else:
    result = (cnt+1)//2
print(result)

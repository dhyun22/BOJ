N, M = map(int, input().split(' '))
DNA = []
result = []


for i in range(N):
    DNA.append(input())
for j in range(M):
    cnt_a = 0
    cnt_t = 0
    cnt_g = 0
    cnt_c = 0
    for k in DNA:
        if k[j] == 'A':
            cnt_a += 1
        if k[j] == 'T':
            cnt_t += 1
        if k[j] == 'G':
            cnt_g += 1
        if k[j] == 'C':
            cnt_c += 1
    if max(cnt_a, cnt_t, cnt_g, cnt_c) == cnt_a:
        result.append('A')
    elif max(cnt_a, cnt_t, cnt_g, cnt_c) == cnt_c:
        result.append('C')
    elif max(cnt_a, cnt_t, cnt_g, cnt_c) == cnt_g:
        result.append('G')
    elif max(cnt_a, cnt_t, cnt_g, cnt_c) == cnt_t:
        result.append('T')

cnt = 0
for m in range(M):
    for n in DNA:
        if n[m] != result[m]:
            cnt += 1

print(''.join(result))
print(cnt)

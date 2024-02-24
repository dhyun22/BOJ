N = int(input())
cnt = 0

for i in range(1, N+1):
    diff_list = []
    if i < 10:
        cnt += 1
    elif i < 100:
        cnt += 1
    elif i < 1000:
        num = list(str(i))
        for j in range(2):
            diff = int(num[j])-int(num[j+1])
            diff_list.append(diff)
        if diff_list[0] == diff_list[1]:
            cnt += 1
    else:
        pass
print(cnt)

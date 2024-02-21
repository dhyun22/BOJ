N = input()
list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in N:
    if i == '6' or i == '9':
        if list[6] == list[9]:
            list[6] += 1
        else:
            list[9] += 1
    else:
        list[int(i)] += 1
answer = max(list)
print(answer)

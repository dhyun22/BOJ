N = int(input())
cnt = 0
for i in range(N):
    word = input()
    if len(word) == 1:
        cnt += 1
    else:
        check = []
        check.append(word[0])
        cnt += 1
        for j in range(len(word)-1):
            if word[j+1] == word[j]:
                continue
            else:
                if word[j+1] in check:
                    cnt -= 1
                    break
                else:
                    check.append(word[j+1])
print(cnt)

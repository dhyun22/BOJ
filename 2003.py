# two pointer 문제 : 시작점과 끝점
# sum 이 m보다 클경우 : left 포인터 뒤로 당겨서 값 줄임
# 작을경우 : right 포인터 뒤로 당겨서 값 늘림
# 같을경우 : cnt +1 하고 left 포인터 뒤로 당기기

N, M = map(int, input().split(' '))
S = list(map(int, input().split(' ')))
cnt = 0
l = 0
r = 0
sum = S[0]


while True:
    if sum == M:
        cnt += 1
        sum -= S[l]
        l += 1
    elif sum < M:
        r += 1
        if r >= N:
            break
        sum += S[r]
    else:
        sum -= S[l]
        l += 1
print(cnt)

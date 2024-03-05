from collections import deque


N, M = map(int, input().split(' '))
queue = deque(range(1, N+1))
position = list(map(int, input().split(' ')))
cnt = 0
for i in position:
    if queue.index(i) >= (len(queue)/2):
        k = len(queue) - queue.index(i)
        cnt += k
        queue.rotate(k)

    else:
        k = queue.index(i)
        cnt += k
        queue.rotate(-k)
    queue.popleft()
print(cnt)

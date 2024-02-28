# list로 풀면 500000일때 시간초과
# Queue 이용

from collections import deque
N = int(input())
Queue = deque(list(range(1, N+1)))


while len(Queue) != 1:
    Queue.popleft()
    Queue.append(0)
    Queue[-1] = Queue[0]
    Queue.popleft()


print(Queue[0])

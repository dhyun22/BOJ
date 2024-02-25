# collection 라이브러리의 deque사용
# 리스트로 구현 시 pop(0)해야 하므로 시간복잡도 O(n)
# deque에서 popleft 사용하면 시간복잡도 O(1)

from collections import deque
import sys

N = int(input())
queue = deque()  # 큐 생성
for i in range(N):
    cmd = sys.stdin.readline().split()  # input().split()으로 하면 시간초과
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif cmd[0] == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)

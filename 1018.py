# 4중 반복문
# 합이 짝/홀인것을 사용
# 복습하기
N, M = map(int, input().split(' '))
board = []
count = []
for i in range(N):
    board.append(input())
for a in range(N-7):
    for b in range(M-7):
        w_index = 0
        b_index = 0
        for k in range(a, a+8):
            for l in range(b, b+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        w_index += 1
                    if board[k][l] != 'B':
                        b_index += 1
                else:
                    if board[k][l] != 'B':
                        w_index += 1
                    if board[k][l] != 'W':
                        b_index += 1
        count.append(w_index)
        count.append(b_index)
print(min(count))

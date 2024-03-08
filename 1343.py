# board = input().split('.')
# board = [i for i in board if i]
# for j in board :
#   if len(j)%2 != 0 :
#     print(-1)
#     break
#   else :
#     if len(j)%4 == 0 :
#       result =

board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)

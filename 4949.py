# from collections import deque
# queue = deque()
while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                print('no')
                break
            out = stack.pop()
            if out != '(':
                print('no')
                break
        elif i == ']':
            if len(stack) == 0:
                print('no')
                break
            out2 = stack.pop()
            if out2 != '[':
                print('no')
                break
        elif i == '.':
            if len(stack) == 0:
                print('yes')
            else:
                print('no')

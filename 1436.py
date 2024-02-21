N = int(input())
A = 666
count = 1
while True:
    if count == N:
        break
    if count != N:
        A += 1
        if '666' in str(A):
            count += 1
print(A)

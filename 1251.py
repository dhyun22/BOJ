A = list(input())
k = len(A)
list = []
m = 1
while m < (k-1):
    n = m+1
    while n < (k):
        print(m, n)
        a = A[0:m]
        b = A[m:n]
        c = A[n:]
        a.reverse()
        a = ''.join(a)
        print(a)
        b.reverse()
        b = ''.join(b)
        print(b)
        c.reverse()
        c = ''.join(c)
        print(c)
        list.append(a+b+c)
        n += 1
    m += 1
print(list)
list.sort()
print(list[0])

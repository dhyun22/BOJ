# set 의 search 는 O(1)
# list의 search 는 O(n)`

N = int(input())
A_set = set(map(int, input().split(' ')))
M = int(input())
B_list = list(map(int, input().split(' ')))

for i in B_list:
    if i in A_set:
        print(1)
    else:
        print(0)

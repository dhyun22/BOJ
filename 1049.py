N, M = map(int, input().split(' '))
set = []
one = []
set_num = N//6
one_num = N % 6
for i in range(M):
    a, b = map(int, input().split(' '))
    set.append(a)
    one.append(b)
min_set = min(set)
min_one = min(one)
if min_set > min_one*one_num:
    if min_set > min_one*6:
        result = min_one*(6*set_num + one_num)
    else:
        result = min_one*one_num + min_set*set_num
else:
    result = min_set*(set_num+1)
print(result)


#     if (a/6) < b < (a/one_num):
#         set.append(a)
#         one.append(b)
#         result.append((a*set_num)+(b*one_num))
#     if b < (a/6):
#         set_each.append(b)
#         result.append((b*6*set_num)+(b*one_num))
#     if b > (a/one_num):
#         one_set.append(a)
#         result.append(a*(set_num+1))
# print(max(result))

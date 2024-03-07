N = int(input())
book = dict()
for i in range(N):
    name = input()
    if name not in book:
        book[name] = 1
    else:
        book[name] += 1
sorted_book = sorted(book.items(), reverse=True, key=lambda item: item[1])
# lambda 함수 써서 dictionary를 값기준으로 내림차순으로 정렬,
# items() 사용 시 key, value 모두 반환 -> 튜플 형식
# values() 사용 시 value만 반환
result = []
for j in sorted_book:
    if j[1] == sorted_book[0][1]:
        result.append(j[0])
result.sort()
print(result[0])

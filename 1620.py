# value로 key값 찾기
# 1대1 대응일 경우 k, v 바꾼 새로운 dict 생성

N, M = map(int, input().split(' '))
pokemon = dict()
for i in range(N):
    pokemon[i+1] = input()
new_pokemon = dict()
for k, v in pokemon.items():
    new_pokemon[v] = k
for j in range(M):
    x = input()
    try:
        print(pokemon[int(x)])
    except:
        print(new_pokemon[x])

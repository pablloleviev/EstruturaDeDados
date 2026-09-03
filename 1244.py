n = int(input())

for _ in range(n):

    palavras = input().split()

    palavras.sort(key=len, reverse=True)

    print(" ".join(palavras))

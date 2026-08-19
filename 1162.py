casos = int(input())

for _ in range(casos):
    n = int(input())

    vagoes = list(map(int, input().split()))

    trocas = 0
    for i in range(1, n):

        J = i

        while J > 0 and vagoes[J] < vagoes[J - 1]:

            vagoes[J], vagoes[J - 1] = vagoes[J - 1], vagoes[J]

            trocas += 1 

            J -= 1
       
print(f"Optimal train swapping takes {trocas} swaps.")

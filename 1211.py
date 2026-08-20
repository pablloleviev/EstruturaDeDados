while True:
    try:
        n = int(input())
    except EOFError:
        break

    telefones = []

    for _ in range(n):
        telefones.append(input().strip())

        telefones.sort()

        economia = 0

        for i in range(1, n):
            anterior = telefones[i - 1]
            atual = telefones[i]

            J = 0
            while J < len(atual) and atual[J] == anterior[J]:
                J += 1
            economia += J

    print(economia)
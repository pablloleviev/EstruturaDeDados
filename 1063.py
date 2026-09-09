import sys


def resolver(chegada, destino):
    pilha = []
    movimentos = []
    indice = 0

    for letra in chegada:
        pilha.append(letra)
        movimentos.append('I')

        while pilha and pilha[-1] == destino[indice]:
            pilha.pop()
            movimentos.append('R')
            indice += 1

            if indice == len(destino):
                return ''.join(movimentos)

    if indice == len(destino):
        return ''.join(movimentos)

    return 'Impossible'


def main():
    dados = sys.stdin.read().split()
    if not dados:
        return

    i = 0
    saidas = []

    while i < len(dados):
        n = int(dados[i])
        i += 1

        if n == 0:
            break

        chegada = dados[i:i + n]
        i += n
        destino = dados[i:i + n]
        i += n

        saidas.append(resolver(chegada, destino))

    sys.stdout.write('\n'.join(saidas))


if __name__ == '__main__':
    main()

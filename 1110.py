from collections import deque  # deque = fila de duas pontas, rápida para tirar/inserir nas extremidades

while True:  # loop infinito: roda até a gente mandar parar (com break)

    N = int(input())  # lê uma linha do teclado e converte de texto para número inteiro

    if N == 0:  # 0 é o sinal de "fim da entrada", conforme o enunciado
        break   # interrompe o while True e encerra o programa

    # cria a fila de cartas de 1 até N (o +1 é necessário porque range() exclui o último número)
    # ex: N=7 -> range(1, 8) -> gera 1, 2, 3, 4, 5, 6, 7
    fila = deque(range(1, N + 1))

    descartados = []  # lista vazia para guardar, em ordem, as cartas que forem descartadas

    while len(fila) > 1:  # repete enquanto houver 2 ou mais cartas na fila

        # tira a carta da frente (popleft) e guarda na lista de descartados
        # str() converte para texto, já que depois vamos juntar tudo com vírgulas
        descartados.append(str(fila.popleft()))

        # tira a próxima carta da frente (popleft) e recoloca no final da fila (append)
        # essa é a carta que "sobrevive" e volta pro fim da pilha
        fila.append(fila.popleft())

    # junta todos os itens da lista de descartados numa única string, separados por ", "
    print("Discarded cards:", ", ".join(descartados))

    # depois que o loop termina, sobra só 1 carta na fila (posição 0) -> é a carta remanescente
    print("Remaining card:", str(fila[0]))
while True: #loop infinito
    try:
        expressao = input()
        
        pilha = []
        correta = True

        for caractere in expressao:

            if caractere == "(":
                pilha.append(caractere)

            elif caractere == ")":

                if len(pilha) == 0:
                    correta = False
                    break
                else:
                    pilha.pop()

        if correta and len(pilha) == 0:
            print("correta")
        else:
            print("incorreta")

    except EOFError:
        break
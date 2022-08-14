import random


def iniciar_a_jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta(nome_arquivo=r"C:\Users\akhen\PycharmProjects\jogos\palavras.txt"):
    palavras = []

    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = (palavras[random.randrange(0, len(palavras))]).upper()
    # .rangrange exclui o último número.
    # P. ex. .randrange(0, 4) exclui o 4.
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def continua_letras_acertadas(letras_acertadas):
    for cada_letra in letras_acertadas:
        print(cada_letra, end=' ')


def imprime_mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print(r"      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print(r"        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def resultado(acertou, palavra_secreta):
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim do jogo")


def marca_chute_correto(palavra_secreta, letras_acertadas, chute):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def marca_chute_errado(erros):
    erros += 1
    print('Ops, você errou! Faltam {} tentativas'.format(7 - erros))
    return erros


def jogar():
    iniciar_a_jogar()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    continua_letras_acertadas(letras_acertadas)

    while not acertou and not enforcou:

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, letras_acertadas, chute)
        else:
            erros = marca_chute_errado(erros)

        enforcou = erros == 7  # True se erros já atingiu 6
        desenha_forca(erros)
        acertou = "_" not in letras_acertadas
        continua_letras_acertadas(letras_acertadas)

    resultado(acertou, palavra_secreta)


if __name__ == "__main__":
    # Ao rodar esse programa diretamente no Prompt de comando, deverá
    # funcionar, mas também se deve evitar que o programa rode
    # imediatamente ao ser chamado por jogar.py.

    # A variável __name__ está com o valor "__main__"? Sim, quando o Python
    # roda diretamente no Prompt de comando.
    jogar()

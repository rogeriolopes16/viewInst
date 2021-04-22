from modules.viewInstagram import *
from random import randint

if __name__ == '__main__':
    quantidade_execucoes = randint(48, 77)

    openInstagram = InstagramBot()
    i = 0
    print(f"Quantidade de vezes a executar: {quantidade_execucoes}.")
    # Execuções dos videos
    while i < quantidade_execucoes:
        print("Execução: " + str(i + 1))
        openInstagram.watch_reels()
        i += 1

    #openInstagram.finaliza()
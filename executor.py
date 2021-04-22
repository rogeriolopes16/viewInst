from modules.viewInstagram import *

if __name__ == '__main__':
    quantidade_execucoes = 30

    openInstagram = InstagramBot()
    i = 0
    # Execuções dos videos
    while i < quantidade_execucoes:
        print("Execução: " + str(i + 1))
        openInstagram.watch_reels()
        i += 1

    #openInstagram.finaliza()
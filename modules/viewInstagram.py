import os
import sys
from selenium import webdriver
import time
from pynput.mouse import Button, Controller
from random import randint, shuffle
import pyperclip


class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"d:/Rogerio/projects/viewYoutube/tools/geckodriver.exe")

    @staticmethod
    def carrega_reels():
        arquivo = open("d:/Rogerio/projects/viewInstagram/parameters/reels.txt", 'r')
        videos = []
        for n in arquivo:
            videos.append(n.strip())
        shuffle(videos)
        return videos

    def watch_reels(self):
        try:
            driver = self.driver
            for video in self.carrega_reels():
                driver.get(video)  # abre o video do indice atual
                print(f"Assistindo o video: {video}.")
                time.sleep(2)  # Tempo que irá assistir o reelsgir
        except:
            driver = self.driver
            driver.close()
            sys.exit()

    def finaliza(self):
        driver = self.driver
        driver.close()
        os.system('shutdown -s')

    @staticmethod
    def captura_ponteiro():
        mouse = Controller()
        time.sleep(2)
        print('The current pointer position is {0}'.format(mouse.position))

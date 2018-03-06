import pygame
import os

version = '2.0 (Beta)'
update = 'March 6th, 2018'


def playlist():
    print(
        "+-----------------------------------------------------------------------------------------------------------+")
    print(
        "|                                                                                                           |")
    print(
        "|                                       KOALA'S JUKEBOX                                                     |")
    print(
        "|                                                                                                           |")
    print(
        "| Version: {}             Created by: Matheus Dias Vieira          Last Update On: {}  |".format(version,
                                                                                                               update))
    print(
        "+-----------------------------------------------------------------------------------------------------------+")

    print('''\nPLAYLIST:\n
    001- Numb - Linkin Park
    002- Sweet Child'O Mine - Guns and Roses
    003- Payphone - Maroon 5 ft. Wiz Khalifa\n''')
    pygame.mixer.init()
    music = pygame.mixer.music
    toca = input('Qual Música tocar?[Diga o número]: ')
    if toca == '001':
        music.load('numb.mp3')
        music.play()
    elif toca == '002':
        music.load('sweet_child_o_mine.mp3')
        music.play()
    elif toca == '003':
        music.load('payphone.mp3')
        music.play()
    else:
        playlist()

    while True:
        esc = input("Queres parar? Y/N: ")
        if esc == 'Y':
            music.fadeout(2000)
            pygame.time.wait(2000)
            pygame.quit()
            os.system('cls')
            playlist()
            break

        elif esc == 'y':
            music.fadeout(2000)
            pygame.time.wait(2000)
            pygame.quit()
            os.system('cls')
            playlist()
            break
        else:
            pass


playlist()

os.system("pause")

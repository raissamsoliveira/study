#Faça um progrma em Pyhron que abra e reproduza o áudio de um arquivo mp3. 

import pygame
pygame.init()
pygame.mixer.music.load ('exe-021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

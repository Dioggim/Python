#from pygame import mixer

#mixer.init()
#mixer.music.load('ex021')
#mixer.music.play()
#paygame.event.wait() #faz o programa esperar para terminar a tarefa em tempo de a musica terminar.
#import time
#time.sleep(360)

import pygame
# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('../Aula 9 - Exercícios 22 ao 27/ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
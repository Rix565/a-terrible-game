import pygame
from time import sleep

#init pygame
pygame.init()

#prepare the game
game = pygame.display.set_mode((800, 600))
pygame.display.set_caption("A terrible game")
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

#load music
pygame.mixer.music.load("sound/main.ogg")
pygame.mixer.music.play()

#load a white background
game.fill((255, 255, 255))
pygame.display.update()

#load copyright image and some random stuff
copyrightimg = pygame.image.load("images/copyright.png")
game.blit(copyrightimg, (362, 250))
pygame.display.flip()
sleep(2.5)
game.fill((255, 255, 255))
pygame.display.update()

#load title screen after that
titleimg = pygame.image.load("images/title_screen.png")
game.blit(titleimg, (192, 25))
pygame.display.flip()

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
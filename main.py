# importer le  module qui contient youtes les
# fonctionnalités python pygame.
import pygame

# initialiser toutes les fonctionnalites.
pygame.init()

# initialiser l'image background
background = pygame.image.load("assets/bg.jpg")

# generer la fenetre de notre jeu
pygame.display.set_caption("The best game")
pygame.display.set_mode((1024, 640))

running = True

# on crée une looop infinie pour garder la fenetre ouverte
while running:

    # on affiche l'image de backgrounsd a l'ecran
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

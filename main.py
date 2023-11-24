# importer le  module qui contient youtes les
# fonctionnalités python pygame.
import pygame

# initialiser toutes les fonctionnalites.
pygame.init()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 2
        self.health = 100
        self.max_health = 100
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500


# initialiser l'image background
background = pygame.image.load("assets/bg.jpg")

# generer la fenetre de notre jeu
pygame.display.set_caption("The best game")
screen = pygame.display.set_mode((1024, 640))

running = True

# on crée une looop infinie pour garder la fenetre ouverte
while running:

    # on affiche l'image de backgrounsd a l'ecran
    screen.blit(background,(0, -300))
    #mettre l'ecran a jour
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

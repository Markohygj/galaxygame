import pygame.display
from pygame import *

pygame.init()

window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__()
        self.speed = speed
        self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
        self.rect = self.player_image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))


background = transform.scale(image.load("fon.jpg"), (700, 500))
ball =  GameSprite("ball.png",100,100,50,50,50)
player =  GameSprite("palkaplayer.png",100,100,50,300,300)
run = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



    #відмалювати екран
    window.blit(background,(0, 0))
    #обєкти
    ball.draw(window)
    player.draw(window)

    pygame.display.flip()
    display.update()
    fps.tick(60)

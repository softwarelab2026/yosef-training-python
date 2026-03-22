import pygame
import random
from planes import Plane

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
LEFT = 1
BACKGROUND_IMAGE = 'img1.jpeg'
REFRESH_RATE = 32
BALL_SIZE = 50
COLL = 50
ROW = 50

pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

img = pygame.image.load(BACKGROUND_IMAGE)
img = pygame.transform.scale(img, (500, 500))

clock = pygame.time.Clock()
planes_list = pygame.sprite.Group()

plane1 = Plane(0, 0)
plane2 = Plane(50, 50)
plane3 = Plane(100, 100)
plane4 = Plane(150, 150)
planes_list.add(plane1, plane2, plane3, plane4)

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    for plane in planes_list:
        pygame.time.wait(1000)
        plane.move_random()


    for plane in planes_list:
        planes_hit_list = pygame.sprite.spritecollide(plane, planes_list, False)
        if not len(planes_hit_list) == 1:
            pygame.time.wait(2000)
            finish = True

    screen.blit(img, (0, 0))
    planes_list.draw(screen)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)

pygame.quit()
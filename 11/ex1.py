import pygame

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450
WHITE = (255, 255, 255)
RED = (255, 0, 0)
IMAGE = "img1.jpeg"

pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")


img = pygame.image.load(IMAGE)
screen.fill(WHITE)
screen.blit(img, (0, 0))
pygame.draw.line(screen, RED, [220, 225], [400, 225], 10)
pygame.display.flip()

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

pygame.quit()
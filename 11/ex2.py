import pygame, math

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450
WHITE = (255, 255, 255)
RED = (255, 0, 0)
IMAGE = "img1.jpeg"
center_x = 225
center_y = 225
length = 350



pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")


img = pygame.image.load(IMAGE)
screen.fill(WHITE)
screen.blit(img, (0, 0))


for i in range(100):
    angle = i * (360 / 100)
    angle = math.radians(angle)
    x = center_x + length * math.cos(angle)
    y = center_y + length * math.sin(angle)
    pygame.draw.line(screen, RED, [center_x, center_y], [x, y], 2)
pygame.display.flip()

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

pygame.quit()
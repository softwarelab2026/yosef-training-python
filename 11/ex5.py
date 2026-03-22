import pygame

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450

IMAGE = "img1.jpeg"
REFRESH_RATE = 40
BALL_RADIUS = 40

RED = (255, 0, 0)
PINK = ((239, 136, 190))
#maouse:
LEFT = 1
SCROLL = 2
RIGHT = 3

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game")

img = pygame.image.load(IMAGE)

player_image = pygame.image.load('pink_plane.png').convert()
player_image = pygame.transform.scale(player_image, (50, 50))
player_image.set_colorkey(PINK)

pygame.mouse.set_visible(False)


mouse_pos_list = []
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN \
            and event.button == LEFT:
            mouse_pos_list.append(pygame.mouse.get_pos())

    screen.blit(img, (0, 0))
    screen.blit(player_image, [220, 300])
   

    clock.tick(REFRESH_RATE)
    pygame.display.flip()

pygame.quit()
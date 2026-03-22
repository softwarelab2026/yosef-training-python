import pygame

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450
RED = (255, 0, 0)
IMAGE = "img1.jpeg"
REFRESH_RATE = 60
BALL_RADIUS = 40

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game")

img = pygame.image.load(IMAGE)

clock = pygame.time.Clock()

ball_x_pos = 40
ball_y_pos = 225

vx = 3
vy = 2

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    screen.blit(img, (0, 0))

    ball_x_pos += vx
    ball_y_pos += vy

    left_wall = ball_x_pos - BALL_RADIUS <= 0
    right_wall = ball_x_pos + BALL_RADIUS >= WINDOW_WIDTH
    up_wall = ball_y_pos - BALL_RADIUS <= 0
    down_wall = ball_y_pos + BALL_RADIUS >= WINDOW_HEIGHT

    if left_wall or right_wall:
        vx = -vx

    if up_wall or down_wall:
        vy = -vy

    pygame.draw.circle(screen, RED, (ball_x_pos, ball_y_pos), BALL_RADIUS)

    pygame.display.flip()
    clock.tick(REFRESH_RATE)

pygame.quit()
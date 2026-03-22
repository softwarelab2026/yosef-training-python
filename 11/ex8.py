import pygame
import random
from shapes import Ball


WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450
REFRESH_RATE = 40
WHITE = (255, 255, 255)
RED = (255, 0, 0)
IMAGE = "img1.jpeg"
MAX_VELOCITY = 5
BALL_RADIUS = 25

LEFT = 1
SCROLL = 2
RIGHT = 3

pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()


img = pygame.image.load(IMAGE)



###########################################
# ball1 = Ball(100, 100)
# ball2 = Ball(200, 200)
# screen.blit(ball1.image, ball1.get_pos())
# screen.blit(ball2.image, ball2.get_pos())

balls_list = pygame.sprite.Group()
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        
        elif event.type == pygame.MOUSEBUTTONDOWN \
            and event.button == LEFT:
            x, y = pygame.mouse.get_pos()
            ball = Ball(x, y)
            vx = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
            vy = random.randint(-MAX_VELOCITY, MAX_VELOCITY)
            ball.update_v(vx, vy)
            balls_list.add(ball)
        
        

    for ball in balls_list:
        ball.update_loc()

        left_wall = ball.rect.left <= 0
        right_wall = ball.rect.right >= WINDOW_WIDTH
        up_wall = ball.rect.top <= 0
        down_wall = ball.rect.bottom >= WINDOW_HEIGHT

        if left_wall or right_wall:
            ball.reverse_x()
        if up_wall or down_wall:
            ball.reverse_y()


    screen.blit(img, (0, 0))
    balls_list.draw(screen)
    pygame.display.flip()
    clock.tick(REFRESH_RATE)


pygame.quit()
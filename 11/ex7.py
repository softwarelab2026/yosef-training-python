import pygame

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450

IMAGE = "img1.jpeg"
SOUND_FILE = "airplane_sound.mp3"
REFRESH_RATE = 40
BALL_RADIUS = 40

RED = (255, 0, 0)
PINK = ((239, 136, 190))
#maouse:
LEFT = 1
SCROLL = 2
RIGHT = 3

pygame.init()
pygame.mixer.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game")

img = pygame.image.load(IMAGE)
pygame.mixer.music.load(SOUND_FILE)

player_image = pygame.image.load('pink_plane.png').convert()
player_image = pygame.transform.scale(player_image, (50, 50))
player_image.set_colorkey(PINK)

#pygame.mouse.set_visible(False)

x, y = 200, 300
mouse_pos_list = []
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

        elif event.type == pygame.MOUSEBUTTONDOWN \
            and event.button == LEFT:
            mouse_pos_list.append(pygame.mouse.get_pos())
            
        elif event.type == pygame.MOUSEBUTTONDOWN \
            and event.button == RIGHT:
            pygame.mixer.music.play()

    screen.blit(img, (0, 0))
    mouse_point = pygame.mouse.get_pos()
    screen.blit(player_image, mouse_point)
    for pos in mouse_pos_list:
        screen.blit(player_image, pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 10
    if keys[pygame.K_RIGHT]:
        x += 10
    if keys[pygame.K_UP]:
        y -= 10
    if keys[pygame.K_DOWN]:
        y += 10
    screen.blit(player_image, (x, y))

    if keys[pygame.K_SPACE]:
        mouse_pos_list.clear()
        screen.blit(img, (0, 0))


    clock.tick(REFRESH_RATE)
    pygame.display.flip()
    
pygame.quit()
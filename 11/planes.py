import pygame
import random

PINK = (239, 136, 190)
MOVING_IMAGE = 'pink_plane.png'
CELL_SIZE = 50
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500


class Plane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Plane, self).__init__()

        self.image = pygame.image.load(MOVING_IMAGE).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(PINK)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y

    def move_random(self):
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)


        new_x = self.rect.x + dx * CELL_SIZE
        new_y = self.rect.y + dy * CELL_SIZE

        if 0 <= new_x < WINDOW_WIDTH and 0 <= new_y < WINDOW_HEIGHT:
            self.rect.x = new_x
            self.rect.y = new_y
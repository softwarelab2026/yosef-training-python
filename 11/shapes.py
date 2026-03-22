import pygame

PINK = (239, 136, 190)
MOVING_IMAGE = 'pink_plane.png'
HORIZONTAL_VELOCITY = 3
VERTICAL_VELOCITY = 5


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Ball, self).__init__()
        self.image = pygame.image.load(MOVING_IMAGE).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.image.set_colorkey(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = HORIZONTAL_VELOCITY
        self.__vy = VERTICAL_VELOCITY

    def update_v(self, vx, vy):      
        self.__vx = vx
        self.__vy = vy
    def update_loc(self):
        self.rect.x += self.__vx
        self.rect.y += self.__vy
    def get_pos(self):
        return self.rect.x, self.rect.y
    def get_v(self):
        return self.__vx, self.__vy
    
    def reverse_x(self):
        self.__vx = -self.__vx
    def reverse_y(self):
        self.__vy = -self.__vy
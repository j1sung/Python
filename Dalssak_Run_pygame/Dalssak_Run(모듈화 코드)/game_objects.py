import pygame
import random
from settings import *

class GameObject:
    def __init__(self, image_path, width, height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

class Barrier(GameObject):
    def __init__(self):
        super().__init__('assets/barrier.png', barrier_width, barrier_height)
        self.reset()

    def reset(self):
        self.rect.x = pad_width
        self.rect.y = random.randrange(0, pad_height - barrier_height)

    def update(self):
        self.rect.x -= 6
        if self.rect.x < 0:
            self.reset()

class Snowball(GameObject):
    def __init__(self):
        super().__init__('assets/snowball.png', snowball_width, snowball_height)
        self.reset()

    def reset(self):
        self.rect.x = pad_width
        self.rect.y = random.randrange(0, pad_height - snowball_height)

    def update(self):
        self.rect.x -= 10
        if self.rect.x < 0:
            self.reset()

class Ice(GameObject):
    def __init__(self):
        super().__init__('assets/ice.png', ice_width, ice_height)
        self.reset()

    def reset(self):
        self.rect.x = pad_width
        self.rect.y = random.randrange(0, pad_height - ice_height)

    def update(self):
        self.rect.x -= 17
        if self.rect.x < 0:
            self.reset()

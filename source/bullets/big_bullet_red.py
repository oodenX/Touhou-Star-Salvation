import random

from source.bullets import bullet
import pygame

from .bullet import Bullet
from .. import constant as C

class BigBulletRed(bullet.Bullet):
    def __init__(self, x, y, target_x, target_y, speed):
        Bullet.__init__(self, x, y, target_x, target_y, speed,48, 32)
        self.image = pygame.image.load(C.big_bullet_red_image)
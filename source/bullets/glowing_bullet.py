import random

from source.bullets import bullet
import pygame

from .bullet import Bullet
from .. import constant as C

class GlowingBullet(bullet.Bullet):
    def __init__(self, x, y, target_x, target_y, speed):
        Bullet.__init__(self, x, y, target_x, target_y, speed, 16, 16)
        self.image = (pygame.image.load(C.glowing_bullet_image)
                      .subsurface((random.randint(0, 7) * 32, 0, 32, 32)))

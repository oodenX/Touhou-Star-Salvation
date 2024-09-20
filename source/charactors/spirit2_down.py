import pygame
import math
from source.bullets.big_bullet_blue import BigBulletBlue
from source.bullets.star_bullet import StarBullet
from source.charactors import enemy
from source import constant as C
from source.bullets.glowing_bullet import GlowingBullet
from source.bullets.circle_bullet import CircleBullet

class Spirit2Down1(enemy.Enemy):
    def __init__(self, x, y, target_x, target_y, speed):
        images = []
        temp = pygame.image.load(C.sprite_image)
        for i in range(0, 6):
            images.append(temp.subsurface(self.get_rect(i, 1)))
        super().__init__(x, y, target_x, target_y, 16, images, 200, speed)
        self.timer = pygame.time.get_ticks()
        self.times = 0

    def shooting(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        super().update(surface, player_bullets)
        if pygame.time.get_ticks() - self.timer >= 50:
            self.timer = pygame.time.get_ticks()
            self.times += 1
        if self.times == 30:
            self.times = 0
            angle = math.degrees(math.atan2(player_y - self.y, player_x - self.x))
            enemy_bullets.append(StarBullet(self.x, self.y, angle, 3))

    def get_rect(self, x, y):
        return pygame.Rect((x * 32, y * 32, 32, 32))

class Spirit2Down2(enemy.Enemy):
    def __init__(self, x, y, target_x, target_y, speed):
        images = []
        temp = pygame.image.load(C.sprite_image)
        for i in range(6, 12):
            images.append(temp.subsurface(self.get_rect(i, 0)))
        super().__init__(x, y, target_x, target_y, 16, images, 200, speed)
        self.timer = pygame.time.get_ticks()
        self.times = 0

    def shooting(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        super().update(surface, player_bullets)
        if pygame.time.get_ticks() - self.timer >= 50:
            self.timer = pygame.time.get_ticks()
            self.times += 1
        if self.times == 30:
            self.times = 0
            angle = math.degrees(math.atan2(player_y - self.y, player_x - self.x))
            enemy_bullets.append(GlowingBullet(self.x, self.y, angle, 3))

    def get_rect(self, x, y):
        return pygame.Rect((x * 32, y * 32, 32, 32))
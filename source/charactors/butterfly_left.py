import pygame

from source.bullets.big_bullet_red import BigBulletRed
from source.charactors import enemy
from source.bullets.glowing_bullet import GlowingBullet
from source.bullets.circle_bullet import CircleBullet

class ButterflyLeft1(enemy.Enemy):
    def __init__(self, x, y, target_x, target_y, speed):
        images = []
        for i in range(1, 6):
            temp = pygame.image.load('./resources/enemy/butterfly_right_' + str(i) + '.png')
            flipped_image = pygame.transform.flip(temp, True, False)
            images.append(flipped_image)
        super().__init__(x, y, target_x, target_y, 32, images, 200, speed)
        self.timer = pygame.time.get_ticks()
        self.times = 0

    def shooting(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        super().update(surface, player_bullets)
        if pygame.time.get_ticks() - self.timer >= 50:
            self.timer = pygame.time.get_ticks()
            self.times += 1
        if self.times == 24:
            self.times = 0
            enemy_bullets.append(BigBulletYellow(self.x, self.y, self.x, self.y + 8, 3))
            enemy_bullets.append(BigBulletYellow(self.x, self.y, self.x, self.y - 8, 3))
            enemy_bullets.append(BigBulletYellow(self.x, self.y, self.x + 8, self.y, 3))
            enemy_bullets.append(BigBulletYellow(self.x, self.y, self.x - 8, self.y, 3))
            enemy_bullets.append(BigBulletYellow(self.x, self.y, self.x - 8, self.y - 8, 3))
            enemy_bullets.append(BigBulletYellow(self.x, self.y, self.x - 8, self.y + 8, 3))
            enemy_bullets.append(BigBulletYellow(self.x, self.y, self.x + 8, self.y - 8, 3))
            enemy_bullets.append(BigBulletYellow(self.x, self.y, self.x + 8, self.y + 8, 3))

class ButterflyLeft2(enemy.Enemy):
    def __init__(self, x, y, target_x, target_y, speed):
        images = []
        for i in range(1, 6):
            temp = pygame.image.load('./resources/enemy/butterfly_right_' + str(i) + '.png')
            flipped_image = pygame.transform.flip(temp, True, False)
            images.append(flipped_image)
        super().__init__(x, y, target_x, target_y, 32, images, 200, speed)
        self.timer = pygame.time.get_ticks()
        self.times = 0

    def shooting(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        super().update(surface, player_bullets)
        if pygame.time.get_ticks() - self.timer >= 50:
            self.timer = pygame.time.get_ticks()
            self.times += 1
        if self.times == 32:
            self.times = 0
            enemy_bullets.append(CircleBullet(self.x, self.y, player_x, player_y, 3))

class ButterflyLeft3(enemy.Enemy):
    def __init__(self, x, y, target_x, target_y, speed):
        images = []
        for i in range(1, 6):
            temp = pygame.image.load('./resources/enemy/butterfly_right_' + str(i) + '.png')
            flipped_image = pygame.transform.flip(temp, True, False)
            images.append(flipped_image)
        super().__init__(x, y, target_x, target_y, 32, images, 200, speed)
        self.timer = pygame.time.get_ticks()
        self.times = 0

    def shooting(self, surface, player_bullets, enemy_bullets, player_x=0, player_y=0):
        super().update(surface, player_bullets)
        if pygame.time.get_ticks() - self.timer >= 50:
            self.timer = pygame.time.get_ticks()
            self.times += 1
        if self.times == 32:
            self.times = 0
            enemy_bullets.append(GlowingBullet(self.x, self.y, player_x, player_y, 3))
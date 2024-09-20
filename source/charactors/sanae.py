import pygame
import math
from numpy.ma.core import angle
from .. import constant as C
from .. import tools
from ..bullets.main_bullet import Bullet
from source.bullets.big_bullet_yellow import BigBulletYellow
from source.bullets.star_bullet import StarBullet
from source.bullets.glowing_bullet import GlowingBullet
from source.bullets.circle_bullet import CircleBullet
from source.bullets.small_star_bullet import SmallStarBullet
from source.charactors import enemy
from source.charactors import myself
import random

class Sanae:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = 39
        self.x = 320
        self.y = 120
        self.speed = 2
        self.timer = pygame.time.get_ticks()
        self.hp = 2500
        self.max_hp = 2500
        self.state = 1
        self.colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255)]
        images = []
        temp = pygame.image.load(C.sanae1_image)
        for i in range(0, 4):
            image = temp.subsurface(self.get_rect(i, 0))
            scaled_image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2))
            images.append(scaled_image)
        self.images1 = images
        images = []
        temp = pygame.image.load(C.sanae2_image)
        for i in range(0, 4):
            image = temp.subsurface(pygame.Rect(i * 63, 0, 63, 63))
            scaled_image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2))
            images.append(scaled_image)
        self.images2 = images
        images = []
        temp = pygame.image.load(C.sanae3_image)
        for i in range(0, 3):
            image = temp.subsurface(pygame.Rect(i * 63, 0, 63, 82))
            scaled_image = pygame.transform.scale(image, (image.get_width() * 1.2, image.get_height() * 1.2))
            images.append(scaled_image)
        self.images3 = images
        self.move_timer = pygame.time.get_ticks()
        self.move_direction = random.choice(['left', 'right', 'up', 'down'])
        self.moving_state_num = 0
        self.magic_circle = pygame.image.load(C.magic_circle_image)
        self.magic_circle_angle = 0
        self.timer1 = pygame.time.get_ticks()
        self.timer2 = pygame.time.get_ticks()
        self.attack_timer = pygame.time.get_ticks()
        self.attack_timer2 = pygame.time.get_ticks()
        self.is_shooting = False
        self.hit = False
        self.alive = True
        self.change_sound = pygame.mixer.Sound(C.sanae_change_sound)

    def get_rect(self, x, y):
        return pygame.Rect((x * 64, y * 64, 64, 64))

    def time_waiting(self):
        if pygame.time.get_ticks() - self.timer1 > 150:
            self.timer1 = pygame.time.get_ticks()
            self.moving_state_num += 1
            if self.moving_state_num == 4:
                self.moving_state_num = 0

    def spinning(self):
        if pygame.time.get_ticks() - self.timer2 > 150:
            self.timer2 = pygame.time.get_ticks()
            self.magic_circle_angle = (self.magic_circle_angle + 15) % 360
            self.magic_circle = pygame.transform.rotate(pygame.image.load(C.magic_circle_image), self.magic_circle_angle)

    def move(self):
        if pygame.time.get_ticks() - self.move_timer > 1500:  # 每1.5秒移动一次
            self.move_timer = pygame.time.get_ticks()
            self.move_direction = random.choice(['left', 'right', 'up', 'down'])

        # 检查是否接近屏幕边缘或下半部分，如果是，则改变方向
        if self.x <= 50:
            self.move_direction = 'right'
        elif self.x >= 590:
            self.move_direction = 'left'
        elif self.y <= 50:
            self.move_direction = 'down'
        elif self.y >= 360:  # 屏幕下半部分的上边界
            self.move_direction = 'up'

        if self.move_direction == 'left':
            self.x -= self.speed
            image = pygame.transform.flip(self.images2[self.moving_state_num], True, False)
        elif self.move_direction == 'right':
            self.x += self.speed
            image = self.images2[self.moving_state_num]
        elif self.move_direction == 'up':
            self.y -= self.speed
            image = pygame.transform.rotate(self.images2[self.moving_state_num], 90)
        elif self.move_direction == 'down':
            self.y += self.speed
            image = pygame.transform.rotate(self.images2[self.moving_state_num], -90)

        # 确保Sanae不会出界
        self.x = max(0, min(self.x, 640 - image.get_width()))
        self.y = max(0, min(self.y, 720 - image.get_height()))

        return image

    def is_dead(self):
        if self.hp <= 0:
            self.state += 1
            if self.state <= 5:
                self.hp = self.max_hp
                self.change_sound.play()  # 播放变换阶段的音效
            else:
                self.alive = False

    def is_hit(self, x, y):
        return (self.x - x) * (self.x - x) + (self.y - y) * (self.y - y) <= self.size * self.size

    def check_hit(self, bullets, Marisa):
        for bullet in bullets:
            if self.is_hit(bullet.center_x, bullet.center_y):
                self.hit = True
                self.hp -= 40
                bullets.remove(bullet)
                Marisa.score += 50
            self.is_dead()

    def draw_health_bar(self, surface):
        if self.state <= 5:
            bar_length = 100
            bar_height = 10
            fill = (self.hp / self.max_hp) * bar_length
            outline_rect = pygame.Rect(10, 10, bar_length, bar_height)
            fill_rect = pygame.Rect(10, 10, fill, bar_height)
            color = self.colors[self.state - 1]
            pygame.draw.rect(surface, color, fill_rect)
            pygame.draw.rect(surface, (255, 255, 255), outline_rect, 2)

    def state_1(self, enemy_bullets):
        if pygame.time.get_ticks() - self.attack_timer > 500:
            self.attack_timer = pygame.time.get_ticks()
            for _ in range(10):
                angle = random.uniform(0, 360)
                bullet = BigBulletYellow(self.x, self.y, angle)
                enemy_bullets.append(bullet)

    def state_2(self, enemy_bullets):
        if pygame.time.get_ticks() - self.attack_timer > 400:
            self.attack_timer = pygame.time.get_ticks()
            for angle in range(0, 360, 30):
                bullet = StarBullet(self.x, self.y, angle)
                enemy_bullets.append(bullet)

    def state_3(self, enemy_bullets):
        if pygame.time.get_ticks() - self.attack_timer > 300:
            self.attack_timer = pygame.time.get_ticks()
            for angle in range(0, 360, 20):
                bullet = GlowingBullet(self.x, self.y, angle)
                enemy_bullets.append(bullet)

    def state_4(self, enemy_bullets, Marisa):
        if pygame.time.get_ticks() - self.attack_timer2 > 200:
            self.attack_timer2 = pygame.time.get_ticks()
            for angle in range(0, 360, 30):
                bullet = SmallStarBullet(self.x, self.y, angle)
                enemy_bullets.append(bullet)
        if pygame.time.get_ticks() - self.attack_timer > 120:
            self.attack_timer = pygame.time.get_ticks()
            angle = self.calculate_angle_to_player(Marisa)
            bullet = StarBullet(self.x, self.y, angle)
            enemy_bullets.append(bullet)

    def state_5(self, enemy_bullets):
        if pygame.time.get_ticks() - self.attack_timer > 200:
            self.attack_timer = pygame.time.get_ticks()
            for angle in range(0, 360, 15):
                bullet = CircleBullet(self.x, self.y, angle)
                enemy_bullets.append(bullet)

    def calculate_angle_to_player(self, Marisa):
        dx = Marisa.center_x - self.x
        dy = Marisa.center_y - self.y
        return math.degrees(math.atan2(dy, dx))

    def update(self, surface, bullets, Marisa, enemy_bullets):
        self.time_waiting()
        self.spinning()
        self.check_hit(bullets, Marisa)
        self.draw_health_bar(surface)
        surface.blit(self.magic_circle, (self.x - self.magic_circle.get_width() // 2, self.y - self.magic_circle.get_height() // 2))

        if self.is_shooting:
            image = self.images3[self.moving_state_num]
        else:
            image = self.move()

        surface.blit(image, (self.x - image.get_width() // 2, self.y - image.get_height() // 2))

        if self.state == 1:
            self.state_1(enemy_bullets)
        elif self.state == 2:
            self.state_2(enemy_bullets)
        elif self.state == 3:
            self.state_3(enemy_bullets)
        elif self.state == 4:
            self.state_4(enemy_bullets, Marisa)
        elif self.state == 5:
            self.state_5(enemy_bullets)

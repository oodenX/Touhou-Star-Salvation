import random

import pygame.time
from .. import constant as C
from source.charactors import myself
from source.game_state import level


class Boss:
    def __init__(self, Marisa):
        self.screen = pygame.display.set_mode(C.size)
        self.background1 = pygame.image.load(C.boss_background)
        self.background2 = pygame.image.load(C.level_background2)
        self.life_text = pygame.image.load(C.life_text)
        self.spell_text = pygame.image.load(C.spell_text)
        self.score_text = pygame.image.load(C.score_text)
        self.power_text = pygame.image.load(C.power_text)
        self.damage_sound = pygame.mixer.Sound(C.damage_sound)
        self.boss_image = pygame.image.load(C.boss_image)
        self.hp = 1000
        self.fire_state = 2
        self.Marisa = Marisa
        self.state = 1
        self.i = 0
        self.moving_state_num = 0
        self.finished = False
        self.next = 'exit'
        self.timer = pygame.time.get_ticks()
        self.timer1 = pygame.time.get_ticks()
        self.timer2 = pygame.time.get_ticks()
        self.timer3 = pygame.time.get_ticks()
        self.timer4 = pygame.time.get_ticks()
        self.timer5 = pygame.time.get_ticks()

        self.score_points = []
        self.power_points = []

    def time_waiting(self):
        if self.timer1 == 0:
            self.timer1 = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer1 > 200:
            self.timer1 = 0
            self.moving_state_num += 1
            if self.moving_state_num == 8:
                self.moving_state_num = 0

    def draw(self, surface, keys):
        font = pygame.font.SysFont('Arial', 36)
        score_text = font.render(str(self.Marisa.score), True, (0, 0, 0))
        life_text = font.render(str(self.Marisa.life), True, (0, 0, 0))
        spell_text = font.render(str(self.Marisa.spell), True, (0, 0, 0))
        power_text = font.render(f'{self.Marisa.power:.2f}', True, (0, 0, 0))
        surface.blit(self.background1, (0, 0))
        surface.blit(self.background2, (640, 0))
        surface.blit(self.life_text, (680, 64))
        surface.blit(life_text, (755, 54))
        surface.blit(self.spell_text, (680, 108))
        surface.blit(spell_text, (740, 98))
        surface.blit(self.score_text, (670, 24))
        surface.blit(score_text, (740, 14))
        surface.blit(self.power_text, (660, 200))
        surface.blit(power_text, (740, 200))
        self.time_waiting()
        player_image = (pygame.image.load(C.player_image).
                        subsurface(self.Marisa.moving_animation(self.moving_state_num, keys)))
        surface.blit(player_image, (self.Marisa.position_x, self.Marisa.position_y))
        if self.Marisa.rate == 0.5:
            surface.blit(self.Marisa.point, (self.Marisa.position_x - 16, self.Marisa.position_y - 8))

    def check_alive(self):
        if self.Marisa.life == 0:
            self.finished = True
            self.next = 'failure'

    # def summon_enemys(self, surface):
    #     for butterfly in self.butterflys:
    #         butterfly.moving_animation(surface, 640, 720)
    #         self.hurt(butterfly.center_x, butterfly.center_y, 35 * 35)
    #         if butterfly.alive == False:
    #             self.butterflys.remove(butterfly)
    #             self.Marisa.score += int(100 * self.Marisa.power)
    #         for bullet in self.Marisa.bullets:
    #             if butterfly.alive:
    #                 butterfly.moving_animation(surface, bullet.center_x, bullet.center_y)
    #                 if butterfly.hit:
    #                     butterfly.hit = False
    #                     self.Marisa.bullets.remove(bullet)
    #                     self.Marisa.score += int(10 * self.Marisa.power)
    #             else:
    #                 # self.butterflys.remove(butterfly)
    #                 self.Marisa.score += int(100 * self.Marisa.power)
    #                 break
    #             self.hurt(butterfly.center_x, butterfly.center_y, 35 * 35)

    def fire_show(self, surface):
        if self.Marisa.nb:
            if self.timer5 == 0:
                self.timer5 = pygame.time.get_ticks()
            elif pygame.time.get_ticks() - self.timer5 > 100:
                self.timer5 = 0
                self.timer5 = pygame.time.get_ticks()
                self.fire_state = random.randint(2, 10)
            image = pygame.image.load(C.fire_image + str(self.fire_state) + '.png')
            surface.blit(image, (self.Marisa.center_x - 6, self.Marisa.center_y + random.randint(-8, 5)))

    def is_nb(self):
        if self.Marisa.nb:
            if pygame.time.get_ticks() - self.timer4 > 3 * C.s:
                self.timer4 = pygame.time.get_ticks()
                self.Marisa.nb = False

    def hurt(self, x, y, para):
        self.is_nb()
        if (self.Marisa.center_x - x) * (self.Marisa.center_x - x) + (self.Marisa.center_y - y) * (
                self.Marisa.center_y - y) <= para:
            if self.Marisa.nb == False:
                self.Marisa.nb = True
                self.Marisa.life -= 1
                self.damage_sound.play()
                self.timer4 = pygame.time.get_ticks()

    def check_point(self, surface):
        for score_point in self.score_points:
            if score_point.state == 2:
                self.score_points.remove(score_point)
                self.Marisa.score += int(150 * self.Marisa.power)
            if score_point.state == 1:
                self.score_points.remove(score_point)
            if score_point.state == 0:
                score_point.update(surface, self.Marisa.center_x, self.Marisa.center_y)
        if self.Marisa.score >= 5000 * pow(2, self.i):
            self.Marisa.life += 1
            self.i += 1

        for power_point in self.power_points:
            if power_point.state == 2:
                self.power_points.remove(power_point)
                self.Marisa.power += 0.05
            if power_point.state == 1:
                self.power_points.remove(power_point)
            if power_point.state == 0:
                power_point.update(surface, self.Marisa.position_x, self.Marisa.position_y)

    def load(self, surface):
        if self.state == 1:
            pass
        elif self.state == 2:
            pass
        elif self.state == 3:
            pass
        elif self.state == 4:
            pass

    def update(self, surface, keys):
        self.draw(surface, keys)
        self.Marisa.update(surface, keys)
        self.check_point(surface)
        self.check_alive()
        self.fire_show(surface)
        self.load(surface)

import pygame
from ..items.score_point import ScorePoint
from ..items.power_point import PowerPoint
from ..charactors.butterfly_down import ButterflyDown1, ButterflyDown2, ButterflyDown3
from ..charactors.butterfly_left import ButterflyLeft1, ButterflyLeft2, ButterflyLeft3
from ..charactors.butterfly_right import ButterflyRight1, ButterflyRight2, ButterflyRight3
from ..bullets.bullet import Bullet
from ..bullets.star_bullet import StarBullet
from ..bullets.big_bullet_red import BigBulletRed
from ..bullets.big_bullet_green import BigBulletGreen
from ..bullets.big_bullet_blue import BigBulletBlue
from ..bullets.big_bullet_yellow import BigBulletYellow
from ..charactors.spirit1_down import Spirit1Down1, Spirit1Down2
from ..charactors.spirit1_left import Spirit1Left1, Spirit1Left2
from ..charactors.spirit1_right import Spirit1Right1, Spirit1Right2
from ..charactors.spirit2_down import Spirit2Down1, Spirit2Down2
from ..charactors.spirit2_left import Spirit2Left1, Spirit2Left2
from ..charactors.spirit2_right import Spirit2Right1, Spirit2Right2
from ..charactors.spirit3_down import Spirit3Down1, Spirit3Down2
from ..charactors.spirit3_left import Spirit3Left1, Spirit3Left2
from ..charactors.spirit3_right import Spirit3Right1, Spirit3Right2
from ..charactors.spirit4_down import Spirit4Down1, Spirit4Down2
from ..charactors.spirit4_left import Spirit4Left1, Spirit4Left2
from ..charactors.spirit4_right import Spirit4Right1, Spirit4Right2

class EnemySummon:
    def __init__(self, enemys):
        self.enemys = enemys
        self.timer = pygame.time.get_ticks()
        self.first_down = False
        self.second_down = False
        self.third_down = False
        self.fourth_down = False
        self.fifth_down = False
        self.sixth_down = False
        self.seventh_down = False
        self.eighth_down = False
        self.ninth_down = False
        self.tenth_down = False
        self.eleventh_down = False
        self.twelfth_down = False
        self.thirteen_down = False
        self.fourteen_down = False
        self.fifteen_down = False
        self.sixteen_down = False
        self.seventeen_down = False
        self.eighteen_down = False
        self.nineteen_down = False
        self.twenty_down = False
        self.twenty_one_down = False
        self.twenty_two_down = False
        self.twenty_three_down = False
        self.twenty_four_down = False
        self.twenty_five_down = False
        self.twenty_six_down = False
        self.twenty_seven_down = False
        self.twenty_eight_down = False
        self.twenty_nine_down = False
        self.thirty_down = False

    def update(self):
        # 第一波出现六只小精灵从左到右
        self.first_wave()
        # 第二波出现六只小精灵从右到左
        self.second_wave()
        # 第三波出现三只蝴蝶
        self.third_wave()
        # 第四波三只蝴蝶下去
        self.forth_wave()
        # 第五波出现左右都依次出现四只小精灵
        self.fifth_wave()
        # 第六波出现三只大蝴蝶
        self.sixth_wave()
        # 第七波出现五只小精灵从上到下
        self.seventh_wave()
        # 第八波出现五只小精灵从下到上
        self.eighth_wave()
        # 第九波出现两只大蝴蝶和四只小精灵
        self.ninth_wave()
        # 第十波出现一只大蝴蝶和六只小精灵
        self.tenth_wave()

    def first_wave(self):
        self.first()
        self.second()
        self.third()
        self.fourth()
        self.fifth()
        self.sixth()

    def second_wave(self):
        self.seventh()
        self.eighth()
        self.ninth()
        self.tenth()
        self.eleventh()
        self.twelfth()

    def third_wave(self):
        self.thirteen()
        self.fourteen()
        self.fifteen()

    def forth_wave(self):
        self.sixteen()
        self.seventeen()

    def fifth_wave(self):
        self.eighteen()
        self.nineteen()
        self.twenty()
        self.twenty_one()
        self.twenty_two()
        self.twenty_three()
        self.twenty_four()
        self.twenty_five()

    def sixth_wave(self):
        self.twenty_six()
        self.twenty_seven()
        self.twenty_eight()

    def seventh_wave(self):
        self.twenty_nine()
        self.thirty()
        self.twenty_one()
        self.twenty_two()
        self.twenty_three()

    def eighth_wave(self):
        self.twenty_four()
        self.twenty_five()
        self.twenty_six()
        self.twenty_seven()
        self.twenty_eight()

    def ninth_wave(self):
        self.twenty_nine()
        self.thirty()
        self.first()
        self.second()
        self.third()
        self.fourth()

    def tenth_wave(self):
        self.fifth()
        self.sixth()
        self.seventh()
        self.eighth()
        self.ninth()
        self.tenth()
        self.eleventh()

    def first(self):
        if pygame.time.get_ticks() > 3000 and self.first_down == False:
            self.first_down = True
            self.enemys.append(Spirit1Right1(0, 40, 640, 60, 3))

    def second(self):
        if pygame.time.get_ticks() > 3300 and self.second_down == False:
            self.second_down = True
            self.enemys.append(Spirit2Right1(0, 40, 640, 60, 3))

    def third(self):
        if pygame.time.get_ticks() > 3600 and self.third_down == False:
            self.third_down = True
            self.enemys.append(Spirit3Right1(0, 40, 640, 60, 3))

    def fourth(self):
        if pygame.time.get_ticks() > 3900 and self.fourth_down == False:
            self.fourth_down = True
            self.enemys.append(Spirit4Right1(0, 40, 640, 60, 3))

    def fifth(self):
        if pygame.time.get_ticks() > 4200 and self.fifth_down == False:
            self.fifth_down = True
            self.enemys.append(Spirit1Right1(0, 40, 640, 60, 3))

    def sixth(self):
        if pygame.time.get_ticks() > 4500 and self.sixth_down == False:
            self.sixth_down = True
            self.enemys.append(Spirit2Right1(0, 40, 640, 60, 3))

    def seventh(self):
        if pygame.time.get_ticks() > 5200 and self.seventh_down == False:
            self.seventh_down = True
            self.enemys.append(Spirit3Left1(640, 60, 0, 40, 3))

    def eighth(self):
        if pygame.time.get_ticks() > 5500 and self.eighth_down == False:
            self.eighth_down = True
            self.enemys.append(Spirit4Left1(640, 60, 0, 40, 3))

    def ninth(self):
        if pygame.time.get_ticks() > 5800 and self.ninth_down == False:
            self.ninth_down = True
            self.enemys.append(Spirit1Left1(640, 60, 0, 40, 3))

    def tenth(self):
        if pygame.time.get_ticks() > 6100 and self.tenth_down == False:
            self.tenth_down = True
            self.enemys.append(Spirit2Left1(640, 60, 0, 40, 3))

    def eleventh(self):
        if pygame.time.get_ticks() > 6400 and self.eleventh_down == False:
            self.eleventh_down = True
            self.enemys.append(Spirit3Left1(640, 60, 0, 40, 3))

    def twelfth(self):
        if pygame.time.get_ticks() > 6700 and self.twelfth_down == False:
            self.twelfth_down = True
            self.enemys.append(Spirit4Left1(640, 60, 0, 40, 3))

    def thirteen(self):
        if pygame.time.get_ticks() > 8000 and self.thirteen_down == False:
            self.thirteen_down = True
            self.enemys.append(ButterflyDown1(50, 100, 50, 100, 4))

    def fourteen(self):
        if pygame.time.get_ticks() > 8000 and self.fourteen_down == False:
            self.fourteen_down = True
            self.enemys.append(ButterflyDown1(300, 60, 300, 60, 4))

    def fifteen(self):
        if pygame.time.get_ticks() > 8000 and self.fifteen_down == False:
            self.fifteen_down = True
            self.enemys.append(ButterflyDown1(580, 100, 580, 100, 4))

    def sixteen(self):
        if pygame.time.get_ticks() > 15000 and self.sixteen_down == False:
            self.sixteen_down = True
            self.enemys.clear()

    def seventeen(self):
        if self.sixteen_down == True and self.seventeen_down == False:
            self.seventeen_down = True
            self.enemys.append(ButterflyDown2(50, 100, 50, 120, 4))
            self.enemys.append(ButterflyDown2(300, 60, 300, 120, 4))
            self.enemys.append(ButterflyDown2(580, 100, 580, 120, 4))

    def eighteen(self):
        if pygame.time.get_ticks() > 17000 and self.eighteen_down == False:
            self.eighteen_down = True
            self.enemys.append(Spirit1Right2(0, 40, 640, 600, 3))

    def nineteen(self):
        if pygame.time.get_ticks() > 17000 and self.nineteen_down == False:
            self.nineteen_down = True
            self.enemys.append(Spirit1Left2(640, 40, 0, 600, 3))

    def twenty(self):
        if pygame.time.get_ticks() > 17500 and self.twenty_down == False:
            self.twenty_down = True
            self.enemys.append(Spirit2Right2(40, 40, 640, 600, 2))

    def twenty_one(self):
        if pygame.time.get_ticks() > 17500 and self.twenty_one_down == False:
            self.twenty_one_down = True
            self.enemys.append(Spirit2Left2(600, 40, 0, 600, 2))

    def twenty_two(self):
        if pygame.time.get_ticks() > 18000 and self.twenty_two_down == False:
            self.twenty_two_down = True
            self.enemys.append(Spirit3Right2(40, 40, 640, 600, 1))

    def twenty_three(self):
        if pygame.time.get_ticks() > 18000 and self.twenty_three_down == False:
            self.twenty_three_down = True
            self.enemys.append(Spirit3Left2(600, 40, 0, 600, 1))

    def twenty_four(self):
        if pygame.time.get_ticks() > 18500 and self.twenty_four_down == False:
            self.twenty_four_down = True
            self.enemys.append(Spirit4Right2(80, 40, 640, 600, 1))

    def twenty_five(self):
        if pygame.time.get_ticks() > 18500 and self.twenty_five_down == False:
            self.twenty_five_down = True
            self.enemys.append(Spirit4Left2(560, 40, 0, 600, 1))

    def twenty_six(self):
        if pygame.time.get_ticks() > 20000 and self.twenty_six_down == False:
            self.twenty_six_down = True
            self.enemys.append(ButterflyDown2(100, 100, 100, 120, 4))

    def twenty_seven(self):
        if pygame.time.get_ticks() > 21000 and self.twenty_seven_down == False:
            self.twenty_seven_down = True
            self.enemys.append(ButterflyDown2(300, 100, 300, 120, 4))

    def twenty_eight(self):
        if pygame.time.get_ticks() > 22000 and self.twenty_eight_down == False:
            self.twenty_eight_down = True
            self.enemys.append(ButterflyDown2(500, 100, 500, 120, 4))

    def twenty_nine(self):
        if pygame.time.get_ticks() > 23000 and self.twenty_nine_down == False:
            self.twenty_nine_down = True
            self.enemys.append(Spirit1Down2(100, 0, 100, 600, 3))

    def thirty(self):
        if pygame.time.get_ticks() > 24000 and self.thirty_down == False:
            self.thirty_down = True
            self.enemys.append(Spirit2Down2(300, 0, 300, 600, 3))
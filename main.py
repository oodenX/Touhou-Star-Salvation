import pygame

from source.game_state import main_menu, level, dialogue, boss, failure
from source import tools
from source.game_state import *

def main():
    # pygame初始化
    pygame.init()
    # 利用字典来传
    state_dict = {
        'main_menu': main_menu.MainMenu(),
        'dialogue': dialogue.Dialogue(),
        'level': level.Level(),
        'failure': failure.Failure()
    }
    game = tools.Game(state_dict, 'main_menu')
    game.run()

# 启动
if __name__ == '__main__':
    main()

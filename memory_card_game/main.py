import pygame
from settings.config import *
from screens.main_menu import main_menu
from screens.game_screen import game_screen

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()

    while True:
        action = main_menu(screen, clock)

        if action == "start":
            while True:
                result = game_screen(screen, clock)
                if result == "restart":
                    continue
                elif result == "menu":
                    break
        elif action == "howto":
            print("게임 설명 준비 중!")
        elif action == "settings":
            print("설정화면 준비 중!")
        else:
            break  # 종료

    pygame.quit()

if __name__ == "__main__":
    main()

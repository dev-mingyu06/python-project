import pygame
from settings.config import *
from screens.main_menu import main_menu
from screens.game_screen import game_screen
from screens.howto_screen import howto_screen

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()

    while True:
        difficulty = main_menu(screen, clock)

        if difficulty in ["easy", "normal", "hard"]:
            while True:
                result = game_screen(screen, clock, difficulty)
                if result == "restart":
                    continue
                elif result == "menu":
                    break
                
        elif difficulty == "howto":
            howto_screen(screen, clock)

        else:
            break
    

    pygame.quit()

if __name__ == "__main__":
    main()

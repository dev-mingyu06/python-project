import pygame
import sys
from settings.config import *

menu = ["GAME START", "SETTING", "HOW TO PLAY", "EXIT"]

def main_menu(screen, clock):
    font = pygame.font.SysFont(None, 50)
    selected_menu = 0
    background = pygame.image.load("C:/Users/chlal/Desktop/상명 25-1/파이썬프로그래밍/memory_card_game/python-project/memory_card_game/assets/images/background.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.blit(background, (0, 0))
        for i, item in enumerate(menu):
            color = (255, 0, 0) if i == selected_menu else (255, 255, 255)
            text = font.render(item, True, color)
            screen.blit(text, (150, 200 + i * 70))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_menu = (selected_menu - 1) % len(menu)
                elif event.key == pygame.K_DOWN:
                    selected_menu = (selected_menu + 1) % len(menu)
                elif event.key == pygame.K_RETURN:
                    selected = menu[selected_menu]
                    print("선택된 항목:",selected)
                    if selected == "GAME START":
                        return "start"
                    elif selected == "HOW TO PLAY":
                        return "howto"
                    elif selected == "SETTING":
                        return "settings"
                    elif selected == "EXIT":
                        pygame.quit()
                        sys.exit()
import pygame
import sys
from settings.config import *

menu = ["EASY MODE", "NORMAL MODE", "HARD MODE", "HOW TO PLAY", "EXIT"]

def main_menu(screen, clock):
    font = pygame.font.SysFont(None, 50)
    selected_menu = 0
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((0, 0, 50))

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
                    if selected == "EASY MODE":
                        return "easy"
                    elif selected == "NORMAL MODE":
                        return "normal"
                    elif selected == "HARD MODE":
                        return "hard"
                    elif selected == "HOW TO PLAY":
                        return "howto"
                    elif selected == "EXIT":
                        pygame.quit()
                        sys.exit()

import pygame
import sys
from settings.config import *

def howto_screen(screen, clock):
    font_title = pygame.font.SysFont(None, 50)
    font_body = pygame.font.SysFont(None, 30)

    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((20, 20, 50))

    instructions = [
        "How to Play",
        "",
        "- Use arrow keys to select a menu item.",
        "- During the game, click two cards to flip them.",
        "- If the cards match, they will stay flipped.",
        "- If they don't match, they will flip back after 1 second.",
        "- Match all pairs to clear the game.",
        "- If time runs out, you lose.",
        "",
        "Press ESC to return to the main menu."
    ]

    while True:
        screen.blit(background, (0, 0))

        for idx, line in enumerate(instructions):
            font = font_title if idx == 0 else font_body
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (80, 80 + idx * 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # 메인 메뉴로 복귀

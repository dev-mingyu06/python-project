import pygame
import sys
from settings.config import *

end_menu = ["RESTART", "MAIN MENU", "EXIT"]

def end_screen(screen, clock, result, playtime):
    pygame.font.init()
    selected = 0
    font_large = pygame.font.SysFont(None, 55)
    font_small = pygame.font.SysFont(None, 35)
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((70, 70, 70))

    while True:
        screen.blit(background, (0, 0))


        if result == "win":
            msg = "CLEAR!" 
            title_text = font_large.render(msg, True, (255, 255, 255))
            screen.blit(title_text, ((SCREEN_WIDTH - title_text.get_width()) // 2, 150))

            time_text = font_small.render(f"CLEAR TIME: {playtime}sec", True, (255, 255, 0))
            screen.blit(time_text, ((SCREEN_WIDTH - time_text.get_width()) // 2, 220))
            
        elif result == "fail":
            msg = "FAIL.."
            title_text = font_large.render(msg, True, (255, 255, 255))
            screen.blit(title_text, ((SCREEN_WIDTH - title_text.get_width()) // 2, 150))
            
        for i, item in enumerate(end_menu):
            color = (255, 0, 0) if i == selected else (255, 255, 255)
            text = font_small.render(item, True, color)
            screen.blit(text, ((SCREEN_WIDTH - text.get_width()) // 2, 300 + i * 60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(end_menu)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(end_menu)
                elif event.key == pygame.K_RETURN:
                    choice = end_menu[selected]
                    if choice == "RESTART":
                        return "restart"
                    elif choice == "MAIN MENU":
                        return "menu"
                    elif choice == "EXIT":
                        pygame.quit()
                        sys.exit()

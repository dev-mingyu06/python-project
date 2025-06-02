import pygame
import sys
from settings.config import *

end_menu = ["RESTART", "MAIN MENU", "EXIT"]

def end_screen(screen, clock, result="win"):
    pygame.font.init()
    selected = 0
    font_large = pygame.font.SysFont(None, 55)
    font_small = pygame.font.SysFont(None, 35)

    # 배경 이미지 불러오기
    if result =="win":
        title_msg = "CLEAR!! PLAY AGAIN?"
        bg_path = "C:/Users/chlal/Desktop/상명 25-1/파이썬프로그래밍/memory_card_game/python-project/memory_card_game/assets/images/clear.png"
    else:
        title_msg = "FAIL... RESTART?"
        bg_path = "C:/Users/chlal/Desktop/상명 25-1/파이썬프로그래밍/memory_card_game/python-project/memory_card_game/assets/images/fail.png"
        
    background = pygame.image.load(bg_path)
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.blit(background, (0, 0))

        # 제목
        title_text = font_large.render(title_msg, True, (0, 0, 0))
        screen.blit(title_text, ((SCREEN_WIDTH - title_text.get_width()) // 2, 150))

        # 메뉴
        for i, item in enumerate(end_menu):
            color = (255, 0, 0) if i == selected else (0, 0, 0)
            text = font_small.render(item, True, color)
            screen.blit(text, ((SCREEN_WIDTH - text.get_width()) // 2, 250 + i * 60))

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
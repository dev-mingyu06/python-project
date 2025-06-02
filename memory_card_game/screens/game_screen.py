import pygame
import random
import sys
from settings.config import *
from logic.card import Card
from logic.matcher import Matcher
from logic.timer import Timer
from screens.end_screen import end_screen

def load_images():
    images = []
    for i in range(1, 16):
        img = pygame.image.load(f"assets/images/card_{i}.png")
        images.append(img)
    back_img = pygame.image.load("assets/images/card_back.png")
    return images, back_img

def create_cards(front_imgs, back_img):
    all_imgs = front_imgs * 2
    ids = list(range(1, 16)) * 2
    combined = list(zip(all_imgs, ids))
    random.shuffle(combined)

    cards = []
    start_x = (SCREEN_WIDTH - (CARD_SIZE[0] + CARD_MARGIN) * GRID_COLS) // 2
    start_y = 80
    for i in range(GRID_ROWS):
        for j in range(GRID_COLS):
            idx = i * GRID_COLS + j
            img, cid = combined[idx]
            x = start_x + j * (CARD_SIZE[0] + CARD_MARGIN)
            y = start_y + i * (CARD_SIZE[1] + CARD_MARGIN)
            resized = pygame.transform.scale(img, CARD_SIZE)
            cards.append(Card(resized, back_img, cid, (x, y)))
    return cards

def game_screen(screen, clock):
    front_imgs, back_img = load_images()
    back_img = pygame.transform.scale(back_img, CARD_SIZE)
    cards = create_cards(front_imgs, back_img)
    matcher = Matcher()
    timer = Timer(TIME_LIMIT)

    running = True
    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not matcher.locked:
                    for card in cards:
                        if card.is_clicked(event.pos):
                            matcher.select(card)
        
        matcher.update()
        
        for card in cards:
            card.draw(screen)

        for card in cards:
            card.draw(screen)

        font = pygame.font.SysFont(None, 36)
        time_text = font.render(f"time: {timer.time_left()}sec", True, (255, 255, 255))
        screen.blit(time_text, (20, 20))

        if all(card.matched for card in cards):
            print("클리어!")
            pygame.time.delay(1000)
            result = end_screen(screen, clock, result="win")
            return result

        if timer.is_time_up():
            print("실패")
            pygame.time.delay(1000)
            result = end_screen(screen, clock, result="fail")
            return result

        pygame.display.flip()
        clock.tick(FPS)

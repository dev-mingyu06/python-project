import pygame, random
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

def create_cards(front_imgs, back_img, pair_count, grid_cols, grid_rows):
    all_imgs = front_imgs[:pair_count] * 2
    ids = list(range(1, pair_count + 1)) * 2
    combined = list(zip(all_imgs, ids))
    random.shuffle(combined)

    cards = []
    start_x = (SCREEN_WIDTH - (CARD_SIZE[0] + CARD_MARGIN) * grid_cols) // 2
    start_y = 80
    for i in range(grid_rows):
        for j in range(grid_cols):
            idx = i * grid_cols + j
            img, cid = combined[idx]
            x = start_x + j * (CARD_SIZE[0] + CARD_MARGIN)
            y = start_y + i * (CARD_SIZE[1] + CARD_MARGIN)
            resized = pygame.transform.scale(img, CARD_SIZE)
            cards.append(Card(resized, back_img, cid, (x, y)))
    return cards

def game_screen(screen, clock, difficulty):
    front_imgs, back_img = load_images()
    back_img = pygame.transform.scale(back_img, CARD_SIZE)
    grid_cols, grid_rows, pair_count = GRID_CONFIG[difficulty]
    cards = create_cards(front_imgs, back_img, pair_count, grid_cols, grid_rows)
    matcher = Matcher()
    timer = Timer(TIME_LIMIT)

    running = True
    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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

        font = pygame.font.SysFont(None, 36)
        time_text = font.render(f"TIME: {timer.time_left()}sec", True, (255, 255, 255))
        screen.blit(time_text, (20, 20))

        if all(card.matched for card in cards):
            pygame.time.delay(1000)
            result = end_screen(screen, clock, "win", timer.elapsed_time())
            return result

        if timer.is_time_up():
            pygame.time.delay(1000)
            result = end_screen(screen, clock, "fail", timer.elapsed_time())
            return result

        pygame.display.flip()
        clock.tick(FPS)

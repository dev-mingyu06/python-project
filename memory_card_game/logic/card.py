import pygame

class Card:
    def __init__(self, front_img, back_img, id, position):
        self.front_img = front_img
        self.back_img = back_img
        self.id = id
        self.rect = pygame.Rect(position, front_img.get_size())
        self.flipped = False
        self.matched = False

    def draw(self, surface):
        if self.flipped or self.matched:
            surface.blit(self.front_img, self.rect.topleft)
        else:
            surface.blit(self.back_img, self.rect.topleft)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos) and not self.flipped and not self.matched

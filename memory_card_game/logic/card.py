import pygame

class Card:
    def __init__(self, image, id, position, size):
        self.image = image
        self.id = id
        self.rect = pygame.Rect(position, size)
        self.fliped = False
        self.matched = False
        self.back_image = None

    def draw(self, surface):
        if self.fliped or self.matched:
            surface.blit(self.image, self.rect)
        else:
            surface.blit(self.back_image, self.rect)
        
    def handle_click(self, pos):
        return self.rect.collidepoint(pos) and not self.fliped and not self.matched
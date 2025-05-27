import time

class Matcher:
    def __init__(self):
        self.selected_cards = []
        
    def select_card(self, card):
        if len(self.selected_cards) < 2:
            card.flipped = True
            self.selected_cards.append(card)
            
    def check_match(self):
        if len(self.selected_cards) == 2:
            a, b = self.selected_cards
            if a.id == b.id:
                a.matched = b.matched = True
                self.selected_cards.clear()
                return True
            return False
        return None
    
    def reset_unmatched(self):
        for card in self.selected_cards:
            card.flipped = False
        self.selected_cards.clear()
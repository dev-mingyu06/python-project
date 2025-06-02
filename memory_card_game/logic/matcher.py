import time

class Matcher:
    def __init__(self):
        self.selected = []
        self.last_check_time = None  # 마지막 두 장을 고른 시간
        self.locked = False          # 잠금 여부 (뒤집는 중일 때 클릭 방지)

    def select(self, card):
        if self.locked or card in self.selected:
            return
        if len(self.selected) < 2:
            card.flipped = True
            self.selected.append(card)
            if len(self.selected) == 2:
                self.last_check_time = time.time()
                self.locked = True

    def update(self):
        if len(self.selected) == 2 and self.locked:
            if time.time() - self.last_check_time >= 1.0:  # 1초 경과
                a, b = self.selected
                if a.id == b.id:
                    a.matched = b.matched = True
                else:
                    a.flipped = b.flipped = False
                self.selected.clear()
                self.locked = False
import pygame
from TextObject import *

class TextInput(TextObject):
    def __init__(self, screen, row_text, pos, font):
        super().__init__(screen, row_text, pos, font)
        self.row_text = row_text
    def update(self, event):
        if event.type == pygame.KEYDOWN:
            print(event.unicode)
            self.row_text += event.unicode
            self.change_text(self.row_text)
            # rect.size = img.get_size()

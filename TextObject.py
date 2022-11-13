import pygame


class TextObject:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, screen, row_text, pos, font, bg="black", feedback=""):
        self.screen = screen
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(row_text, bg)

    def change_text(self, row_text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(row_text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x-self.size[0]//2, self.y-self.size[1]//2, self.size[0], self.size[1])

    def show(self):
        self.screen.blit(self.surface, (self.x-self.size[0]//2, self.y-self.size[1]//2))

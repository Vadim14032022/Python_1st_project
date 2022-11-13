import pygame


class TextObject:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, screen, row_text, pos, font_size, bg="black"):
        self.row_text = row_text
        self.screen = screen
        self.x, self.y = pos
        self.font_size = font_size
        self.font = pygame.font.SysFont("Arial", font_size)
        self.change_text(row_text, bg)

    def change_text(self, row_text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(row_text[:20], 1, pygame.Color("Blue"))
        self.size = max((200,self.font_size),self.text.get_size())
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.fill('white', (2, 2, self.size[0]-4, self.size[1]-4))
        self.surface.blit(self.text, (0, 0))
        #pygame.draw(self.surface, (255,0,0), pygame.Rect(10, 25, 200, 65), 4)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        self.screen.blit(self.surface, (self.x, self.y))

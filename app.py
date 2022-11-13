import pygame
from Button import *
from TextInput import *
from pygame.locals import *
import os
import re

pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((0,0), pygame.RESIZABLE, pygame.FULLSCREEN)
clock = pygame.time.Clock()

text = 'this text is editable'
font = pygame.font.SysFont(None, 40)
img = font.render(text, True, (255, 0, 0))

rect = (20, 50)  # img.get_rect()
# rect.topleft = (20, 20)
# cursor = Rect(rect.topright, (3, rect.height))

print(screen.get_width(), screen.get_height())
#bt = Button(screen, "Click here", (screen.get_width()//2, screen.get_height()//2+100),  font_size=70, bg = 'red', color="navy")
path = os.path.join(os.path.dirname(__file__),'app_texts','text2.txt')
text = ' '.join(open(path).readlines())
text = re.sub(r"[^a-zA-Z0-9 ]","",text)
print(text)
ti = DoubleTextInput(screen, text, (screen.get_width()//2, screen.get_height()//2), 50, size = (900, 50))
running = True
n = 0


while running:
    for event in pygame.event.get():
        #bt.click(event)
        ti.update(event)
        #if event.key == pygame.K_ESCAPE:
        #   running = False
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    #bt.show()
    ti.show()
    #screen.blit(font.render(str(int(pygame.time.get_ticks() / 1000)), True, (0, 255, 0)), (10, 25))
    #pygame.draw.rect(screen, (255,0,0), Rect(10, 25, 200, 65), 4)
    #screen.blit(img, rect)

    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (screen.get_width()/2, screen.get_height()/2), 75)

    # Flip the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(120)

pygame.quit()
exit()

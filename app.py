from Windows import *

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE, pygame.FULLSCREEN)

window_print_text = WindowPrintText(screen, 'text2.txt')

while True:
    window_print_text.run()

pygame.quit()
exit()

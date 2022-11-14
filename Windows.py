import os
import re
import time

from TextInput import *


class WindowMenu():
    def __init__(self):
        pass


class WindowPrintText():
    def __init__(self, screen, file_name):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.end_time = time.time()
        self.objects = []
        path = os.path.join(os.path.dirname(__file__), 'app_texts', file_name)
        text = ' '.join(open(path).readlines())
        self.text = re.sub(r"[^a-zA-Z0-9 ]", "", text)
        self.ti = DoubleTextInput(screen, self.text, (screen.get_width() // 2, screen.get_height() // 2), 50,
                                  bg=(135, 206, 250),
                                  size=(900, 50))
        self.text_time = TextObject(screen, "{:.2f}".format(self.end_time - self.start_time),
                                    (screen.get_width() // 2 - 400, screen.get_height() // 2 - 150), 50,
                                    color="gray",
                                    bg=(135, 206, 250))
        self.text_speed = TextObject(screen, "0", (screen.get_width() // 2, screen.get_height() // 2 - 150), 50,
                                     color="gray",
                                     bg=(135, 206, 250))
        self.text_mistakes = TextObject(screen, "0", (screen.get_width() // 2 + 400, screen.get_height() // 2 - 150),
                                        50,
                                        color="gray",
                                        bg=(135, 206, 250))
        self.text_word_time = TextObject(screen, "Время",
                                         (screen.get_width() // 2 - 400, screen.get_height() // 2 - 208), 50,
                                         color="gray",
                                         bg=(135, 206, 250))
        self.text_word_speed = TextObject(screen, "Скорость", (screen.get_width() // 2, screen.get_height() // 2 - 208),
                                          50,
                                          color="gray",
                                          bg=(135, 206, 250))
        self.text_word_mistakes = TextObject(screen, "Точность",
                                             (screen.get_width() // 2 + 400, screen.get_height() // 2 - 208),
                                             50,
                                             color="gray",
                                             bg=(135, 206, 250))

        self.start = False
        self.end = False

    def run(self):
        running = True

        while running:

            for event in pygame.event.get():
                self.ti.update(event)
                self.press_key(event)
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

            self.screen.fill((135, 206, 250))
            self.ti.show()
            self.update_fields()
            self.text_word_time.show()
            self.text_time.show()

            self.text_word_speed.show()
            self.text_speed.show()

            self.text_word_mistakes.show()
            self.text_mistakes.show()

            pygame.display.flip()
            self.clock.tick(120)

    def press_key(self, event):
        if event.type == pygame.KEYDOWN:
            if self.ti.printed == 1 and not self.start:
                self.start = True
                self.start_time = time.time()
            if self.ti.printed == len(self.text) and not self.end:
                self.end = True
                self.end_time = time.time()

    def update_fields(self):
        if self.start and not self.end:
            print("{:.2f}".format(time.time() - self.start_time))
            self.text_time.change_text("{:.2f}".format(time.time() - self.start_time))
            self.text_speed.change_text("{:.0f}".format(self.ti.printed / (time.time() - self.start_time) * 60))
            self.text_mistakes.change_text("{:.2f}".format(1 - self.ti.mistakes / self.ti.printed))
        if self.end:
            self.text_time.change_text("{:.2f}".format(self.end_time - self.start_time))
            self.text_speed.change_text("{:.0f}".format(self.ti.printed / (self.end_time - self.start_time) * 60))
            self.text_mistakes.change_text("{:.2f}".format(1 - self.ti.mistakes / self.ti.printed))

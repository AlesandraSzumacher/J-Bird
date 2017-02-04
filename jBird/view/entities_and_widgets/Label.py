import pygame


class Label:
    def create(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        return surface

    def write_text(self, window, text, text_color, length, height, x, y):
        font_size = int(length // len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        window.blit(myText, ((x + length / 2) - myText.get_width() / 2, (y + height / 2) - myText.get_height() / 2))
        return window
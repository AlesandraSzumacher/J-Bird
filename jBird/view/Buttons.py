import pygame

pygame.init()


class Button:
    def create(self, window, color, x, y, length, height, width, text, text_color):
        window = self.draw(window, color, length, height, width, x, y)
        window = self.write_text(window, text, text_color, length, height, width, x, y)
        self.rect = pygame.Rect(x, y, length, height)
        return window

    def write_text(self, window, text, text_color, length, height, width, x, y):
        font_size = int(length // len(text))
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        window.blit(myText, ((x + length / 2) - myText.get_width() / 2, (y + height / 2) - myText.get_height() / 2))
        return window

    def draw(self, window, color, length, height, x, y, width):
        for i in range(1, 10):
            s = pygame.Surface((length + (i * 2), height + (i * 2)))
            s.fill(color)
            alpha = (255 / (i + 2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x - i, y - i, length + i, height + i), width)
            window.blit(s, (x - i, y - i))
        pygame.draw.rect(window, color, (x, y, length, height), 0)
        pygame.draw.rect(window, (190, 190, 190), (x, y, length, height), 1)
        return window

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0] and mouse[1] < self.rect.bottomright[1] and mouse[1] > self.rect.topleft[1] < self.rect.bottomright[0] :
            print("Some button was pressed!")
            return True
        else:
            return False

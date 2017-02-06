import pygame

from jBird.control.ButtonControl import ButtonControl

pygame.init()


class Button:
    """Class containing methods which display buttons."""

    def create(self, screen, color, x, y, length, height, width, text, text_color):
        """Creating new button."""
        screen = self.draw_button(screen, color, length, height, x, y, width)
        screen = self.write_text(screen, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x, y, length, height)
        self.buttonClick = ButtonControl()
        return screen

    def draw_button(self, screen, color, length, height, x, y, width):
        """Drawing button."""
        for i in range(1, 10):
            s = pygame.Surface((length + (i * 2), height + (i * 2)))
            s.fill(color)
            alpha = (255 / (i + 2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x - i, y - i, length + i, height + i), width)
            screen.blit(s, (x - i, y - i))
        pygame.draw.rect(screen, color, (x, y, length, height), 0)
        pygame.draw.rect(screen, (190, 190, 190), (x, y, length, height), 1)
        return screen

    def write_text(self, window, text, text_color, length, height, x, y):
        """Writing text on the button."""
        font_size = int(length // len(text))
        myFont = pygame.font.SysFont("monospace", font_size, True)
        myText = myFont.render(text, 1, text_color)
        window.blit(myText, ((x + length / 2) - myText.get_width() / 2, (y + height / 2) - myText.get_height() / 2))
        return window

    def pressed(self, mouse):
        """Checking if button is pressed."""
        return self.buttonClick.pressed(self.rect, mouse)

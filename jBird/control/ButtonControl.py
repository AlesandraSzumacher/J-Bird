class ButtonControl:
    """ Containing methods which handle button operations."""
    def pressed(self, rect, mouse):
        """Handling pressing the button."""
        return mouse[0] > rect.topleft[0] and mouse[1] < rect.bottomright[1] and mouse[1] > rect.topleft[1] < rect.bottomright[0]
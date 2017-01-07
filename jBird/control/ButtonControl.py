class ButtonControl:
    def pressed(self, rect, mouse):
        if mouse[0] > rect.topleft[0] and mouse[1] < rect.bottomright[1] and mouse[1] > rect.topleft[1] < rect.bottomright[0] :
            print("Some button was pressed!")
            return True
        else:
            return False

# Button class 
import pygame

from sorting_visualizer.gui.draw import DrawInformation



class Button:
    # ... existing code ...
    def __init__(self, x, y, width, height, text, color, font, font_color=DrawInformation.BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.font = font
        self.font_color = font_color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.font_color)
        window.blit(text_surface, (
            self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
            self.rect.y + (self.rect.height - text_surface.get_height()) // 2
        ))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

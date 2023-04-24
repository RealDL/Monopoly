import pygame

class Text(object):
    def __init__(self, text, x=700, y=440, height=0):
        self.text = text
        self.x = x
        self.y = y
        self.height = height
        self.textSize = 32
        self.base_font = pygame.font.SysFont("comicsans", self.textSize)
    def draw(self, win):
        surface_area = self.base_font.render(self.text, 1, (0,0,0))
        win.blit(surface_area, (self.x, self.y + (self.height/2 - surface_area.get_height()/2)))
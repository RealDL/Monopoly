import pygame

class TextBox(object):
    def __init__(self, width, height, x, y):
        self.text = ''
        self.textSize = 32
        self.base_font = pygame.font.SysFont("comicsans", self.textSize)
        self.active = False
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color_active = pygame.Color(200,200,200)
        self.color_passive = pygame.Color(150,150,150)
        self.color = self.color_passive
    def draw(self, win):
        area = [self.x,self.y,self.width,self.height]
        pygame.draw.rect(win, self.color, area, 2)
    def checkTextBox(self):
        mouse = pygame.mouse.get_pos()
        if self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y:
            self.active = True
        else:
            self.active = False

        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive
    def update(self, win,font_style="comicsans",x_pos=None,y_pos=None):
        if x_pos == None:
            """If an x pos is given"""
            x_pos = self.x
        if y_pos == None:
            """If a y pos is given"""
            y_pos = self.y
        if self.text != '':
            """Updates the text with the newText, the font and x and y. the old text is removed"""
            #self.text += newText
            surface_area = self.base_font.render(self.text, 1, (0,0,0))
            text_width = surface_area.get_width() + 10 # add some padding
            if text_width > self.width:
                self.width = text_width
            win.blit(surface_area, (x_pos + 5, y_pos + (self.height/2 - surface_area.get_height()/2)))
        #else:
         #   surface_area = self.base_font.render(self.text, 1, (0,0,0))
          #  win.blit(surface_area, (x_pos + 5, y_pos + (self.height/2 - surface_area.get_height()/2)))

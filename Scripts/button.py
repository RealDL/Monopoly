import pygame

class Button():
    """A class for all buttons"""
    def __init__(self, color, color2, x, y, width=None, height=None, text='',buttonType='', radius=None, textSize=30):
        """Sets the values for buttton"""
        self.color = color
        self.color2 = color2
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.buttonType = buttonType
        self.radius = radius
        self.textSize = textSize
        self.hover = False
        self.click = False

    def draw(self,win,outline=None,action=None,font_style="comicsans"):
        """Draws the button. Variable for mouse detection"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.buttonType == "Rectangle":
            """If it is a rectangle it will draw it here"""
            if outline:
                """draws an outline"""
                pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            if self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y:
                """Draws a lighter version of the image"""
                pygame.draw.rect(win, self.color2, (self.x,self.y,self.width,self.height),0)
                self.hover = True
                
                if click[0] == 1:
                    self.click = True
                    if action != None:
                        """If there is an action it is run"""
                        action()
                else:
                    """When mouse is not clicking"""
                    self.click = False
            else:
                self.hover = False
                """A darker version of image when the player isn't hovering over"""
                pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)             
            
            if self.text != '':
                """Text is blit here"""
                font = pygame.font.SysFont(font_style, self.textSize)
                text = font.render(self.text, 1, (0,0,0))
                win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        if self.buttonType == "Circle":
            """If it is a circle it will draw it here"""
            if outline:
                """draws an outline"""
                pygame.draw.circle(win, outline, (self.x, self.y),self.radius+4,0)
            """Trig for area"""
            differenceInX = mouse[0] - self.x
            differenceInY = mouse[1] - self.y
            difference = ( differenceInX**2 + differenceInY**2 )**0.5
            """Print info on the circle"""
            ## print("\n" + "Circle X: " + str(self.x) + "\nCircle Y: " + str(self.y) + "\nMy X: " + str(mouse[0]) + "\nMy Y: " + str(mouse[1]) + "\nDifference in X: " + str(differenceInX)+ "\nDifference in Y: " + str(differenceInY) + "\nDifference: " + str(difference) + "\nRadius: " + str(self.radius) + "\n")
            if difference <= self.radius:
                """Draws a lighter version of the image"""
                pygame.draw.circle(win, self.color2, (self.x,self.y),self.radius,0)
      
                if click[0] == 1 and action != None:
                    """If there is an action it is run"""
                    action()
            else:
                """A darker version of image when the player isn't hovering over"""
                pygame.draw.circle(win, self.color, (self.x,self.y),self.radius,0)
             
            
            if self.text != '':
                """Text is blit here"""
                font = pygame.font.SysFont(font_style, self.textSize)
                text = font.render(self.text, 1, (0,0,0))
                win.blit(text, (self.x - (text.get_width()/2), self.y - (text.get_height()/2)))
                
    def update(self, win ,newText,font_style="comicsans",x_pos=None,y_pos=None):
        if x_pos == None:
            """If an x pos is given"""
            x_pos = self.x
        if y_pos == None:
            """If a y pos is given"""
            y_pos = self.y
        if newText != '':
            """Updates the text with the newText, the font and x and y. the old text is removed"""
            self.text = None
            font = pygame.font.SysFont(font_style, self.textSize)
            text = font.render(newText, 1, (0,0,0))
            win.blit(text, (x_pos + (self.width/2 - text.get_width()/2), y_pos + (self.height/2 - text.get_height()/2)))

    
import pygame, webbrowser, time
print(pygame.font.get_fonts())
class WordButton(object):
    def __init__(self, y, x, text, color1, color2, textSize=30):
        """Sets the values for button"""
        self.color = color1 #(220, 59, 102)
        self.color2 = color2 #(169, 25, 64) 
        self.x = x
        self.y = y
        self.text = text
        self.textSize = textSize
        self.largeSize = round(self.textSize * 1.25)
        self.base_font = pygame.font.Font("Fonts/Monopoly_Regular.ttf", self.textSize)
        self.large_font = pygame.font.Font("Fonts/Monopoly_Bold.ttf", self.largeSize)
        self.hover = False
        self.click = False
        self.release = False

    def displayText(self, win, newText=None, action=None, link=None):
        if newText != None:
            self.text = newText
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Render text with both fonts
        text = self.large_font.render(self.text, 1, self.color2)
        text2 = self.base_font.render(self.text, 1, self.color)

        # Check if mouse is over the text
        if self.x + text.get_width()/2> mouse[0] > self.x - text.get_width()/2 and self.y + text.get_height()/2  > mouse[1] > self.y - text.get_height()/2:
            self.hover = True
            # Render text with larger font and lighter color
            text = self.large_font.render(self.text, 1, self.color2)

            # Center text vertically as well as horizontally
            win.blit(text, (self.x - text.get_width() / 2, self.y - text.get_height() / 2))

            # Check for mouse click and run action if specified
            if click[0] == 1:
                self.click = True
            
            if self.click == True and not click[0]:
                self.release = True
            
            if self.release:
                if action != None:
                    action()
                if link != None:
                    webbrowser.open(link)
                self.release = False
                self.click = False
        else:
            self.hover = False
            self.click = False
            self.release = False
            # Render text with base font and color
            text2 = self.base_font.render(self.text, 1, self.color)

            # Center text vertically as well as horizontally
            win.blit(text2, (self.x - text2.get_width() / 2, self.y - text2.get_height() / 2))



class Animation(object):
    def __init__(self, win, image, scale, scale_direction, scale_min, scale_max, scale_speed, screen_y):
        self.scale = scale #1.0
        self.image = image
        self.scale_direction = scale_direction #-1.35  # Start by zooming out
        self.scale_min = scale_min #0.9
        self.scale_max = scale_max #1.2
        self.scale_speed = scale_speed #0.01  # The rate at which the scale changes
        self.screen_center_x = win.get_width() // 2
        self.screen_center_y = screen_y #324#win.get_height() // 2
        self.monopoly_rect = self.image.get_rect(center=(self.screen_center_x, self.screen_center_y))

    def animation(self, win):
        self.scale += self.scale_direction * self.scale_speed
        if self.scale <= self.scale_min:
            if self.scale_direction < 0:
                self.scale_direction = self.scale_direction * -1
            else:
                self.scale_direction = self.scale_direction * 1# Start zooming in
        elif self.scale >= self.scale_max:
            if self.scale_direction > 0:
                self.scale_direction = self.scale_direction * -1
            else:
                self.scale_direction = self.scale_direction * 1  # Start zooming out

        # Scale the image and get its rect
        scaled_monopoly = pygame.transform.rotozoom(self.image, 0, self.scale)
        scaled_monopoly_rect = scaled_monopoly.get_rect(center=(self.screen_center_x, self.screen_center_y))

        # Blit the scaled image to the screen and update the display
        win.blit(scaled_monopoly, scaled_monopoly_rect)

class TextBox(object):
    def __init__(self, width, height, x, y, color1=(200,200,200), color2=(150,150,150)):
        self.text = ''
        self.textSize = 60
        self.base_font = pygame.font.SysFont("lucidabright", self.textSize)
        self.active = False
        self.width = width
        self.height = height
        self.x = x - self.width / 2
        self.ogWidth = width
        self.y = y
        self.color_active = pygame.Color(color1)
        self.color_passive = pygame.Color(color2)
        self.color = self.color_passive
        self.last_update = 0 # time of last update
        self.show_cursor = False # whether to show cursor or not
        
    def draw(self, win):
        area = [self.x,self.y,self.width,self.height]
        pygame.draw.rect(win, self.color, area, 2, 10)
        
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
        middleOfX = win.get_width() // 2
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
            text_width = surface_area.get_width() + 20 # add some padding
            if self.ogWidth > self.width:
                    self.width = self.ogWidth
                    self.x = middleOfX - self.width / 2

            if text_width > self.width:
                print("one")
                self.width = text_width
                self.x = middleOfX - self.width / 2
            elif self.width > text_width:
                if self.ogWidth < self.width:
                    print("two")
                    self.width = text_width
                    self.x = middleOfX - self.width / 2
            win.blit(surface_area, (x_pos + 5, y_pos + (self.height/2 - surface_area.get_height()/2)))
        #else:
         #   surface_area = self.base_font.render(self.text, 1, (0,0,0))
          #  win.blit(surface_area, (x_pos + 5, y_pos + (self.height/2 - surface_area.get_height()/2)))
        
        # show typing animation
        time_since_last_update = pygame.time.get_ticks() - self.last_update
        if self.active and time_since_last_update > 500:
            self.show_cursor = not self.show_cursor # toggle cursor visibility
            self.last_update = pygame.time.get_ticks() # update last_update time

        if self.show_cursor:
            text_to_show = self.text + '|' # add cursor to end of text
        else:
            text_to_show = self.text # do not show cursor
            
        surface_area = self.base_font.render(text_to_show, 1, (0,0,0))
        win.blit(surface_area, (x_pos + 5, y_pos + (self.height/2 - surface_area.get_height()/2)))


class Text(object):
    def __init__(self, text, x=700, y=440, height=0):
        self.text = text
        self.x = x
        self.y = y
        self.height = height
        self.textSize = 32
        self.base_font = pygame.font.Font("Fonts/Monopoly_Regular.ttf", self.textSize)
    def draw(self, win):
        surface_area = self.base_font.render(self.text, 1, (0,0,0))
        win.blit(surface_area, (self.x - surface_area.get_width() / 2, self.y - surface_area.get_height() / 2))
    def update(self, win, newtext, color):
        self.text = newtext
        surface_area = self.base_font.render(self.text, 1, color)
        win.blit(surface_area, (self.x - surface_area.get_width() / 2, self.y - surface_area.get_height() / 2))

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
        self.base_font = pygame.font.SysFont("Fonts/Monopoly_Regular.ttf", self.textSize)
    def draw(self,win,outline=None,action=None,font_style="comicsans", colorChange=True):
        """Draws the button. Variable for mouse detection"""
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.buttonType == "Rectangle":
            """If it is a rectangle it will draw it here"""
            if outline:
                """draws an outline"""
                pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0,20)
            if self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y and colorChange:
                """Draws a lighter version of the image"""
                pygame.draw.rect(win, self.color2, (self.x,self.y,self.width,self.height),0,20)
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
                pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0, 20)             
            
            if self.text != '':
                """Text is blit here"""
                text = self.base_font.render(self.text, 1, (0,0,0))
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
                text = self.base_font.render(self.text, 1, (0,0,0))
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
            text = self.base_font.render(newText, 1, (0,0,0))
            win.blit(text, (x_pos + (self.width/2 - text.get_width()/2), y_pos + (self.height/2 - text.get_height()/2)))

    
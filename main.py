import pygame, sys, random
from Scripts.button import Button
from Scripts.player import Player
from Scripts.game import Game
from Scripts.setup import Setup
from Scripts.textbox import TextBox
from Scripts.text import Text

def quit_game():
    """Stop the music and close the game"""
    ## pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()
    quit()

def StartingScreen():
    def redrawWindow():
        """A function in a function that redraws the background image and the start and quit buttons"""
        
        win.blit(startScreenBG, (0,0))
        startButton.draw(win,(0,0,0),SetupUpGame)
        quitButton.draw(win,(0,0,0),quit_game)
        #cursor()
        
    while setup.startScreen:
        """Checks if player wants to quit application"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game()

        """The window is redrawn, display is updated and the clock speed ticks by 60."""
        redrawWindow()
        pygame.display.update()
        clock.tick(CLOCKSPEED)

def SetupUpGame():
    setup.startScreen = False
    setup.numberOfPlayerInGame = True
    def check():
        try:
            number = int(numberOfplayers.text)
            if number >=2 and number <=6:
                return number
        except:
            print("Do nothing")

    def redrawWindow():
        """A function in a function that redraws the background image and the start and quit buttons"""
        
        win.blit(lockerRoomBG, (0,0))
        numberOfplayersText.draw(win)
        numberOfplayers.draw(win)
        numberOfplayers.update(win)
        #cursor()
        
    while setup.numberOfPlayerInGame:
        """Checks if player wants to quit application"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                numberOfplayers.checkTextBox()
            if event.type == pygame.KEYDOWN:
                if numberOfplayers.active == True:
                    if event.key == pygame.K_BACKSPACE:
                        numberOfplayers.text = numberOfplayers.text[0:-1]
                    elif event.key == pygame.K_RETURN:
                        passedOrNot = check()
                        if passedOrNot:
                            print(passedOrNot)
                            chooseCharacter(passedOrNot)
                        else:
                            numberOfplayers.text = ''
                    else:
                        numberOfplayers.text += event.unicode
                if event.key == pygame.K_ESCAPE:
                    quit_game()

        """The window is redrawn, display is updated and the clock speed ticks by 60."""
        redrawWindow()
        pygame.display.update()
        clock.tick(CLOCKSPEED)

def chooseCharacter(numberOfPlayersPlaying):
    setup.numberOfPlayerInGame = False
    setup.setUp = True
    gameSetup = Game(numberOfPlayersPlaying)
    tokens = ["Images/Tokens/car.png","Images/Tokens/dog.png","Images/Tokens/hat.png","Images/Tokens/iron.png","Images/Tokens/ship.png","Images/Tokens/shoe.png","Images/Tokens/thimble.png","Images/Tokens/wheel.png"]
    players = []

    def check():
        if gameSetup.playerNumberInterval >= 1:
            username = tempTextBoxForName.text
            token = random.choice(tokens)
            tokens.remove(token)
            player = Player(username, token)
            players.append(player)
            gameSetup.playerNumberInterval -= 1
            print(username, token)
            print(tokens)
        
    def setupCharacter():
        tempOverButton.draw(win,(0,0,0))
        tempNameText.draw(win)
        tempTextBoxForName.draw(win)
        tempTextBoxForName.update(win)
        if gameSetup.playerNumberInterval < 1:
            MainGame()


    def redrawWindow():
        """A function in a function that redraws the background image and the start and quit buttons"""
        win.blit(lockerRoomBG, (0,0))
        setupCharacter()
        #cursor()
        
    while setup.setUp:
        """Checks if player wants to quit application"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    tempTextBoxForName.checkTextBox()
            if event.type == pygame.KEYDOWN:
                if tempTextBoxForName.active == True:
                    if event.key == pygame.K_BACKSPACE:
                        tempTextBoxForName.text = tempTextBoxForName.text[0:-1]
                    elif event.key == pygame.K_RETURN:
                        check()
                        tempTextBoxForName.text = ''
                    else:
                        tempTextBoxForName.text += event.unicode
                if event.key == pygame.K_ESCAPE:
                    quit_game()

        """The window is redrawn, display is updated and the clock speed ticks by 60."""
        redrawWindow()
        pygame.display.update()
        clock.tick(CLOCKSPEED)

def MainGame():
    setup.setUp = False
    setup.MainGame = True

    def turn():
        pass
        ## Show a button
        ## With a title saying money.
        ## They with there money and username and token.
        ## Properties
        
    def characters():
        pass
        ## Draw there tokens here.

    def redrawWindow():
        """A function in a function that redraws the background image and the start and quit buttons"""
        win.blit(board, (0,0))
        #cursor()
        
    while setup.MainGame:
        """Checks if player wants to quit application"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game()

        """The window is redrawn, display is updated and the clock speed ticks by 60."""
        redrawWindow()
        pygame.display.update()
        clock.tick(CLOCKSPEED)

pygame.init()
#pygame.mouse.set_visible(False)
win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Monopoly!")
clock = pygame.time.Clock()
CLOCKSPEED = 60

""" Images """
gameIcon = pygame.image.load("Images/icon.jpg")
pygame.display.set_icon(gameIcon)
startScreenBG = pygame.image.load("Images/monopolystart.jpg").convert()
lockerRoomBG = pygame.image.load("Images/lockerroom.png").convert()
board  = pygame.image.load("Images/board.png").convert()
# mainScreenBG = pygame.image.load("Images/mainscreen.png").convert()

""" Audio """
setup = Setup()

"""Setup"""


""" All the different buttons """
startButton = Button((0,200,0),(0,255,0),710,750,100,50,"Start!","Rectangle",None,30)
quitButton = Button((200,0,0),(255,0,0),1010,750,100,50,"Quit!","Rectangle",None,30)
numberOfplayers = TextBox(450, 100, 735, 490)
numberOfplayersText = Text("Enter the number of players below:")

## Buttons for character choose
tempOverButton = Button((105,24,226),(129,51,246),660,290,600,500,"","Rectangle",None,30)
tempNameText = Text("Enter your username below: ",750,400,0)
tempTextBoxForName = TextBox(450, 100, 735, 490)

""" The if statement the will run the program - Loading up the game """
if __name__ == "__main__":
    try:
        """If there is nothing wrong with the code etc it will run startScreen"""
        StartingScreen()
    except Exception as Error:
        """If there is an Error with some of the code, the Error is printed and the game is quit"""
        print(Error)
        quit_game()
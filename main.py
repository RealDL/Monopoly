import pygame, random, time
from Scripts.functions import Button, Text, TextBox, Animation, WordButton
from Scripts.player import Player
from Scripts.game import Game, Setup

def StartingScreen():
    def redrawWindow():
        """A function in a function that redraws the background image and the start and quit buttons"""
        numberOfPlayerText = "Play with " + str(setup.players) + " Players"
        monopolyBackgroundAnimation.animation(win)
        monopolyAnimation.animation(win)
        startButton.displayText(win, None, chooseCharacter)
        infoButton.displayText(win, None, None, "https://www.hasbro.com/common/instruct/00009.pdf")
        playerButton.displayText(win, numberOfPlayerText)
        AddPlayerButton.displayText(win, None, setup.AddPlayers)
        MinusPlayerButton.displayText(win, None, setup.RemovePlayer)
        quitButton.displayText(win, None, setup.QuitGame)
        #cursor()
        
    while setup.startScreen:
        """Checks if player wants to quit application"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                setup.QuitGame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    setup.QuitGame()

        """The window is redrawn, display is updated and the clock speed ticks by 60."""
        redrawWindow()
        pygame.display.update()
        clock.tick(CLOCKSPEED)

def chooseCharacter():
    setup.startScreen = False
    setup.setUp = True
    gameSetup = Game(setup.players)
    tokens = ["Images/Tokens/car.png","Images/Tokens/dog.png","Images/Tokens/hat.png","Images/Tokens/iron.png","Images/Tokens/ship.png","Images/Tokens/shoe.png","Images/Tokens/thimble.png","Images/Tokens/wheel.png"]
    players = []

    def check():
        if gameSetup.playerNumberInterval <= setup.players and tempTextBoxForName.text != "":
            username = tempTextBoxForName.text
            token = random.choice(tokens)
            tokens.remove(token)
            player = Player(username, token)
            players.append(player)
            gameSetup.playerNumberInterval += 1
            tempTextBoxForName.text = ''

            print(username, token)
            print(tokens)
        
    def setupCharacter():
        
        tempOverButton.draw(win,(0,0,0), None, None, False)
        tempNameText.draw(win)
        player = "Player " + str(gameSetup.playerNumberInterval+1) + ", enter your name below."
        tempNameText.update(win, player, (220,220,220))
        tempTextBoxForName.checkTextBox()
        tempTextBoxForName.draw(win)
        tempTextBoxForName.update(win)
        if gameSetup.playerNumberInterval >= setup.players:
            MainGame()


    def redrawWindow():
        """A function in a function that redraws the background image and the start and quit buttons"""
        monopolyBackgroundAnimation.animation(win)
        setupCharacter()
        nextButton.displayText(win, None, check)
        #cursor()
        
    while setup.setUp:
        """Checks if player wants to quit application"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                setup.QuitGame()
          
            if event.type == pygame.MOUSEBUTTONDOWN:
                    tempTextBoxForName.checkTextBox()
            if event.type == pygame.KEYDOWN:
                if tempTextBoxForName.active == True:
                    if event.key == pygame.K_BACKSPACE:
                        tempTextBoxForName.text = tempTextBoxForName.text[0:-1]
            
                    elif event.key == pygame.K_DELETE:
                        tempTextBoxForName.text = ''
            
                    else:
                        tempTextBoxForName.text += event.unicode
            
                if event.key == pygame.K_ESCAPE:
                    setup.QuitGame()

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
                setup.QuitGame()            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    setup.QuitGame()

        """The window is redrawn, display is updated and the clock speed ticks by 60."""
        redrawWindow()
        pygame.display.update()
        clock.tick(CLOCKSPEED)

"""Setting Up the Game"""
pygame.init()
#pygame.mouse.set_visible(False)
win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Monopoly!")
clock = pygame.time.Clock()
CLOCKSPEED = 60
middleOfX = win.get_width() // 2
setup = Setup()

""" Images """
gameIcon = pygame.image.load("Images/icon.jpg").convert()
pygame.display.set_icon(gameIcon)
startScreenBG = pygame.image.load("Images/StartScreen/background.png").convert()
board  = pygame.image.load("Images/board.png").convert()
monopoly = pygame.image.load("Images/StartScreen/monopoly.png").convert()
# mainScreenBG = pygame.image.load("Images/mainscreen.png").convert()

"""Animations"""
monopolyBackgroundAnimation = Animation(win, startScreenBG, 1.0, 0.005, 0.9, 1.3, 0.55, 540)
monopolyAnimation = Animation(win, monopoly, 1.0, 0.005, 0.9, 1.1, 2.2, 324)

""" All the different buttons """
##WordButtons
AddPlayerButton = WordButton(765, middleOfX-210, "+", (220, 59, 102), (169, 25, 64), 40)
MinusPlayerButton = WordButton(765, middleOfX+210, "-", (220, 59, 102), (169, 25, 64), 40)
playerButton = WordButton(765, middleOfX, "Play with 2 Players", (220, 59, 102), (169, 25, 64), 40)
startButton = WordButton(700, middleOfX, "Play Monopoly!", (220, 59, 102), (169, 25, 64), 40)
infoButton = WordButton(830, middleOfX, "How To Play Monopoly", (220, 59, 102), (169, 25, 64), 40)
quitButton = WordButton(895, middleOfX, "Quit!", (220, 59, 102), (169, 25, 64), 40)
nextButton = WordButton(700, middleOfX, "Continue!", (12, 182, 29), (40, 220, 58), 40)

## Buttons for character choose
tempOverButton = Button((56,56,203),(129,51,246),660,290,600,500,"","Rectangle",None,30)
tempNameText = Text("Player 1 enter your name:",middleOfX,400,0)
tempTextBoxForName = TextBox(450, 100, middleOfX, 490)

""" The if statement the will run the program - Loading up the game """
if __name__ == "__main__":
    try:
        """If there is nothing wrong with the code etc it will run startScreen"""
        StartingScreen()
    except Exception as Error:
        """If there is an Error with some of the code, the Error is printed and the game is quit"""
        print(Error)
        setup.QuitGame()

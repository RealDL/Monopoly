"""All functions"""
def StartingScreen():
    def redrawWindow():
        """A function in a function that redraws the background image and the start and quit buttons"""
        numberOfPlayerText = "Play with " + str(setup.NumberOfPlayers) + " Players"
        monopolyBackgroundAnimation.animation(setup.win)
        monopolyAnimation.animation(setup.win)
        startButton.displayText(setup.win, None, chooseCharacter)
        infoButton.displayText(setup.win, None, None, "https://www.hasbro.com/common/instruct/00009.pdf")
        playerButton.displayText(setup.win, numberOfPlayerText)
        AddPlayerButton.displayText(setup.win, None, setup.AddPlayers)
        MinusPlayerButton.displayText(setup.win, None, setup.RemovePlayer)
        quitButton.displayText(setup.win, None, setup.QuitGame)
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
        setup.clock.tick(setup.CLOCKSPEED)

def chooseCharacter():
    setup.startScreen = False
    setup.setUp = True
    gameSetup = Game(setup.NumberOfPlayers)
    setup.game = gameSetup
    
    def check():
        setup.notSameUsername = True
        if setup.game.playerNumberInterval <= setup.NumberOfPlayers:
            if setup.players != []:
                for numOfplayers in setup.players:
                    if numOfplayers.username == tempTextBoxForName.text:
                        setup.notSameUsername = False
            if setup.notSameUsername and tempTextBoxForName.text != "":
                setup.errorPopup = False
                username = tempTextBoxForName.text
                token = setup.tokens[setup.imageInterval]
                setup.imageInterval = 0
                setup.tokens.remove(token)
                players = Player(username, token, setup.NumberOfPlayers)
                setup.players.append(players)
                setup.game.playerNumberInterval += 1
                tempTextBoxForName.text = ''
                tempTextBoxForName.cursor = 0

                print(username,token)
                print(setup.tokens)
            else:
                setup.errorPopup = True
            #error popup?
        
    def setupCharacter():
        if len(setup.tokens) >= 1:
            tempOverButton.draw(setup.win,(0,0,0), None, None, False)
            imageButton.draw(setup.win, (0,0,0), None, None, False)
            imageCoverButton.draw(setup.win)
            setup.draw(setup.win, 896, 537)
            nextleftButton.displayText(setup.win, None, setup.decreaseImageInterval)
            nextrightButton.displayText(setup.win, None, setup.increaseImageInterval)
            player = "Player " + str(setup.game.playerNumberInterval+1) + ", enter your name and choose your token below."
            tempNameText.draw(setup.win)
            tempNameText.update(setup.win, player, (220,220,220))
            #tempTextBoxForName.checkTextBox()
            tempTextBoxForName.draw(setup.win)
            tempTextBoxForName.update(setup.win)
        if setup.game.playerNumberInterval >= setup.NumberOfPlayers:
            MainGame()


    def redrawWindow():
        def removePopup():
            setup.errorPopup = False
        """A function in a function that redraws the background image and the start and quit buttons"""
        monopolyBackgroundAnimation.animation(setup.win)
        setupCharacter()
        nextButton.displayText(setup.win, None, check)
        if setup.errorPopup:
            errorButton.draw(setup.win, (0,0,0))
            errorText2.update(setup.win, "You cannot have a duplicate or empty username.", (0,0,0))
            errorText.update(setup.win, "Error! Please make sure you have a valid username!", (0,0,0))
            errorClose.displayText(setup.win, None, removePopup)
        #cursor()
        
    while setup.setUp:
        """Checks if player wants to quit application"""
        events = pygame.event.get()
        tempTextBoxForName.updateText(events, check)
        for event in events:
            if event.type == pygame.QUIT:
                setup.QuitGame()
          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    setup.QuitGame()

        """The window is redrawn, display is updated and the clock speed ticks by 60."""
        redrawWindow()
        pygame.display.update()
        setup.clock.tick(setup.CLOCKSPEED)

def MainGame():
    setup.mixUpPlayerOrder()
    setup.setUp = False
    setup.MainGame = True
    
    def showEvent():
        player = setup.players[setup.playerTurn]
        if player.displayEvent == True:
            eventButton.draw(setup.win, (0,0,0))
            eventHeader.update(setup.win, player.title, (250,30,10))
            eventText.update(setup.win, player.information, (0,0,0))
            eventClose.displayText(setup.win, None, closeEvent)
        
    def closeEvent():
        player = setup.players[setup.playerTurn]
        if player.displayEvent == True:
            player.displayEvent = False

    def EndTurnFunction():
        player = setup.players[setup.playerTurn]
        if player.playerTurn:
            setup.turns()
            player.EndTurn()

    def move():
        player = setup.players[setup.playerTurn]
        player.Roll()
        if player.givePlayerMoney:
            for eachPlayer in setup.players:
                if eachPlayer.givePlayerMoney != True:
                    eachPlayer.money += 50
                    eachPlayer.networth += 50
            player.givePlayerMoney = False
        
        if player.recieveMoneyFromPlayers:
            for eachPlayer in setup.players:
                if eachPlayer.recieveMoneyFromPlayers != True:
                    eachPlayer.money -= 10
                    eachPlayer.networth -= 10
            player.recieveMoneyFromPlayers = False

    def GetOutOfJailFunction():
        player = setup.players[setup.playerTurn]
        player.GetOutOfJail() 

    def turn():
        ## Player
        player = setup.players[setup.playerTurn]
        playerinfoButton.draw(setup.win, (0,0,0))
        playerInformation.draw(setup.win, (0,0,0))
        playerInfo.update(setup.win, "Player's Information:", (255,255,255))
        playerName.update(setup.win, "Username: " + str(player.username), (148,148,148))
        playerMoney.update(setup.win, "Money: " + "$" + str(player.money), (148,148,148))
        playerNetworth.update(setup.win, "Networth: " + "$" + str(player.networth), (148,148,148))
        playerTokenInfo.update(setup.win, "Player's Token:", (255,255,255))
        playerInJail.update(setup.win, "Currently in Jail: " + str(player.inJail), (148,148,148))
        playerToken.draw(setup.win, (0,0,0))
        player.draw(setup.win, 149, 406)
        playerProperties.update(setup.win, "Player's Properties:", (255,255,255))
        playerButtonToSeeProperties.displayText(setup.win, None,None)

        ## Die
        roleDieButton.draw(setup.win, (0,0,0))
        roleDieWordButton.draw(setup.win, (0,0,0))
        redRoleButton.draw(setup.win, (0,0,0))
        dieRole.displayText(setup.win, None, move)
        endTurnButton.draw(setup.win, (0,0,0))
        endTurn.displayText(setup.win, None, EndTurnFunction)

        ## Jail
        getOutOfJail.draw(setup.win, (0,0,0))
        getOutOfJalText.displayText(setup.win, None, GetOutOfJailFunction)
        
    def characters():
        for char in setup.players:
            char.screen(setup.win)

        ## Draw there tokens here.

    def redrawWindow():
        """A function in a function that redraws the background image and the start and quit buttons"""
        board.draw(setup.win)
        turn()
        characters()
        showEvent()
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
        setup.clock.tick(setup.CLOCKSPEED)

"""Setting Up the Game with imports and variables"""
import pygame, random, time
from Scripts.functions import Button, Text, TextBox, Animation, WordButton, Images
from Scripts.game import Game, Setup, Player

pygame.init()
#pygame.mouse.set_visible(False)
pygame.display.set_caption("Monopoly!")
setup = Setup()


""" Images """
gameIcon = Images("Images/icon.jpg")
gameIcon.display_icon()
startScreenBG = Images("Images/General/background.png")
board  = Images("Images/General/board.png")
monopoly = Images("Images/General/monopoly.png")

"""Animations"""
monopolyBackgroundAnimation = Animation(startScreenBG.load_image, 1.0, 0.005, 0.9, 1.3, 0.55, 540, setup.middleOfX)
monopolyAnimation = Animation(monopoly.load_image, 1.0, 0.005, 0.9, 1.1, 3, 324, setup.middleOfX)

""" All the different buttons """
## Start Screen buttons
AddPlayerButton = WordButton(765, setup.middleOfX-210, "+", (220, 59, 102), (169, 25, 64), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)
MinusPlayerButton = WordButton(765, setup.middleOfX+210, "-", (220, 59, 102), (169, 25, 64), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)
playerButton = WordButton(765, setup.middleOfX, "Play with 2 Players", (220, 59, 102), (169, 25, 64), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)
startButton = WordButton(700, setup.middleOfX, "Play Monopoly!", (220, 59, 102), (169, 25, 64), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)
infoButton = WordButton(830, setup.middleOfX, "How To Play Monopoly", (220, 59, 102), (169, 25, 64), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)
quitButton = WordButton(895, setup.middleOfX, "Quit!", (220, 59, 102), (169, 25, 64), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)

## Buttons for character choose
nextButton = WordButton(780, setup.middleOfX, "Continue!", (12, 182, 29), (40, 220, 58), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)
nextleftButton = WordButton(600, setup.middleOfX-150, "<", (20,20,20), (0,0,0), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)
nextrightButton = WordButton(600, setup.middleOfX+150, ">", (20,20,20), (0,0,0), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)
tempOverButton = Button((56,56,203),(129,51,246),560,240,800,600,"","Rectangle",None,30)
imageButton = Button((56,56,203),(255,0,0),760,500,400,200,"","Rectangle",None,20)
imageCoverButton = Button((0,0,0),(0,0,0),890,530,140,140,"","Rectangle",None,15)
tempNameText = Text("Player 1, enter your name and choose your token below.",setup.middleOfX,300,"Fonts/Monopoly_Regular.ttf",32)
tempTextBoxForName = TextBox(650, 100, setup.middleOfX, 340, (200,200,200), (150,150,150), "Fonts/Roboto-Regular.ttf", 10, 2, 350)

## Buttons for character choose: Error Popup
errorButton = Button((215,16,16),(215,16,16),610,390,700,300,"","Rectangle",None,15)
errorText = Text("",setup.middleOfX,setup.middleOfY-110,"Fonts/Monopoly_Regular.ttf",32)
errorText2 = Text("",setup.middleOfX,setup.middleOfY-75,"Fonts/Monopoly_Regular.ttf",32)
errorClose = WordButton(600, setup.middleOfX, "Close", (0, 0, 0), (0, 0, 0), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)

## Buttons for main screen
playerinfoButton = Button((121,193,229),(121,193,229),13,90,400,900,"","Rectangle",None,15)
playerInformation = Button((58,110,213),(58,110,213),38,110,350,860,"","Rectangle",None,15)
playerToken = Button((0,0,0),(0,0,0),138,395,150,150,"","Rectangle",None,15)
playerInfo = Text("",207,140,"Fonts/Monopoly_Bold.ttf",40)
playerName = Text("",207,190,"Fonts/Monopoly_Regular.ttf",32)
playerMoney = Text("",207,225,"Fonts/Monopoly_Regular.ttf",32)
playerNetworth = Text("",207,260,"Fonts/Monopoly_Regular.ttf",32)
playerProperties = Text("",207,600,"Fonts/Monopoly_Bold.ttf",40)
playerTokenInfo = Text("",207,345,"Fonts/Monopoly_Bold.ttf",40)
playerButtonToSeeProperties = WordButton(650,207,"Your Properties",(148,148,148),(148,148,148), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 32)
playerInJail = Text("",207,295,"Fonts/Monopoly_Regular.ttf",32)

##Go button
roleDieButton = Button((121,193,229),(121,193,229),1507,90,400,900,"","Rectangle",None,15)
roleDieWordButton = Button((255,255,255),(255,255,255),1532,110,350,860,"","Rectangle",None,15)
redRoleButton = Button((22,255,27),(22,255,27),1707,230,None,None,"","Circle",100,15)
dieRole = WordButton(230,1707,"Roll!",(0,0,0),(0,0,0), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 50)
endTurnButton = Button((222,27,27),(222,27,27),1707,450,None,None,"","Circle",100,15)
endTurn = WordButton(450,1707,"End Go!",(0,0,0),(0,0,0), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 40)

##Jail
getOutOfJail = Button((255,112,17),(255,112,17),1607,574,200,200,"","Rectangle",None,15)
getOutOfJalText = WordButton(674,1707,"Get Out of Jail!",(0,0,0),(0,0,0), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 25)

##Event
eventButton = Button((255,255,255),(255,255,255),610,390,700,300,"","Rectangle",None,15)
eventHeader = Text("",960,540-100,"Fonts/Monopoly_Bold.ttf",40)
eventText = Text("",960,540-50,"Fonts/Monopoly_Regular.ttf",25)
eventClose = WordButton(540+120,960,"Close",(200,40,20),(255,20,10), "Fonts/Monopoly_Regular.ttf", "Fonts/Monopoly_Bold.ttf", 25)
""" The if statement the will run the program - Loading up the game """
#if __name__ == "__main__":
#    try:
#        """If there is nothing wrong with the code etc it will run startScreen"""
#        StartingScreen()
#    except Exception as Error:
#        """If there is an Error with some of the code, the Error is printed and the game is quit"""
#        print(Error)
#        setup.QuitGame()


StartingScreen()

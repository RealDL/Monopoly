import random, pygame, sys

class Setup(object):
    def __init__(self):
        self.startScreen = True
        self.setUp = False
        self.playerTurn = 0
        self.MainGame = False
        self.NumberOfPlayers = 2
        self.win = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.CLOCKSPEED = 60
        self.imageInterval = 0
        self.middleOfX = self.win.get_width() // 2
        self.middleOfY = self.win.get_height()//2
        self.errorPopup = False
        self.players = []
        self.tokens = ["Images/Tokens/car.png","Images/Tokens/dog.png","Images/Tokens/hat.png","Images/Tokens/iron.png","Images/Tokens/ship.png","Images/Tokens/shoe.png","Images/Tokens/thimble.png","Images/Tokens/wheel.png"]
    def AddPlayers(self):
        if self.NumberOfPlayers < 8:
            self.NumberOfPlayers +=1
    def RemovePlayer(self):
        if self.NumberOfPlayers > 2:
            self.NumberOfPlayers -= 1
    def turns(self):
        if self.playerTurn + 1 < self.NumberOfPlayers:
            self.playerTurn += 1
        else:
            self.playerTurn = 0

    def QuitGame(self):
        """Stop the music and close the game"""
        ## pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()
    def increaseImageInterval(self):
        if self.imageInterval < len(self.tokens)-1:
            self.imageInterval += 1
        else:
            self.imageInterval = 0
        print(self.imageInterval)
    def decreaseImageInterval(self):
        if self.imageInterval > 0:
            self.imageInterval -= 1
        else:
            self.imageInterval = len(self.tokens)-1
        print(self.imageInterval)
    def draw(self, win, x, y):
        image = self.tokens[self.imageInterval]
        load_image = pygame.image.load(image).convert()
        win.blit(load_image, (x,y))
    def mixUpPlayerOrder(self):
        random.shuffle(self.players)
        print(self.players)

class Game(object):
    def __init__(self, numberOfPlayers, numberOfDie=2):
        self.hotels = 12
        self.houses = 32
        self.numberOfPlayers = numberOfPlayers
        self.numberOfDie = numberOfDie
        self.parkFreeMoney = 0
        self.chanceCards = 16
        self.communityCards = 16
        self.propertyNumber = 22
        self.stations = 4
        self.utilities = 2
        self.bank = 20580
        self.passGoMoney = 200
        self.tax = 100
        self.super_tax = 200
        self.board_spaces = 40
        self.playerNumberInterval = 0
        self.board = {
            "GO": {"board_position": 0},
            "Old Kent Road": {"board_position": 1},
            "Community Chest": {"board_position": 2},
            "Whitechapel Road": {"board_position": 3},
            "Income Tax": {"board_position": 4},
            "King's Cross station": {"board_position": 5},
            "The Angel Islington": {"board_position": 6},
            "Chance": {"board_position": 7},
            "Euston Road": {"board_position": 8},
            "Pentonville Road": {"board_position": 9},
            "Jail": {"board_position": 10},
            "Pall Mall": {"board_position": 11},
            "Electric Company": {"board_position": 12},
            "Whitehall": {"board_position": 13},
            "Northumberland Avenue": {"board_position": 14},
            "Marylebone station": {"board_position": 15},
            "Bow Street": {"board_position": 16},
            "Community Chest": {"board_position": 17},
            "Marlborough Street": {"board_position": 18},
            "Vine Street": {"board_position": 19},
            "Free Parking": {"board_position": 20},
            "The Strand": {"board_position": 21},
            "Chance": {"board_position": 22},
            "Fleet Street": {"board_position": 23},
            "Trafalgar Square": {"board_position": 24},
            "Fenchurch Street station": {"board_position": 25},
            "Leicester Square": {"board_position": 26},
            "Coventry Street": {"board_position": 27},
            "Water Works": {"board_position": 28},
            "Piccadilly": {"board_position": 29},
            "Go To Jail": {"board_position": 30},
            "Regent Street": {"board_position": 31},
            "Oxford Street": {"board_position": 32},
            "Community Chest": {"board_position": 32},
            "Bond Street": {"board_position": 34},
            "Liverpool Street station": {"board_position": 35},
            "Chance": {"board_position": 36},
            "Park Lane": {"board_position": 37},
            "Super Tax": {"board_position": 38},
            "Mayfair": {"board_position": 39}
        }
        self.properties = {
            "Old Kent Road": {"price": 60, "mortgage": 30, "mortgaged": False, "owned": False, "house_price": 50, "hotel_price": 250},
            "Whitechapel Road": {"price": 60, "mortgage": 30, "mortgaged": False, "owned": False, "house_price": 50, "hotel_price": 250},
            "King's Cross station": {"price": 200, "mortgage": 100, "mortgaged": False, "owned": False, "house_price": None, "hotel_price": None},
            "The Angel Islington": {"price": 100, "mortgage": 50, "mortgaged": False, "owned": False, "house_price": 50, "hotel_price": 250},
            "Euston Road": {"price": 100, "mortgage": 50, "mortgaged": False, "owned": False, "house_price": 50, "hotel_price": 250},
            "Pentonville Road": {"price": 120, "mortgage": 60, "mortgaged": False, "owned": False, "house_price": 50, "hotel_price": 250},
            "Pall Mall": {"price": 140, "mortgage": 70, "mortgaged": False, "owned": False, "house_price": 100, "hotel_price": 500},
            "Electric Company": {"price": 150, "mortgage": "75", "mortgaged": False, "owned": False, "house_price": None, "hotel_price": None},
            "Whitehall": {"price": 140, "mortgage": 70, "mortgaged": False, "owned": False, "house_price": 100, "hotel_price": 500},
            "Northumberland Avenue": {"price": 160, "mortgage": 80, "mortgaged": False, "owned": False, "house_price": 100, "hotel_price": 500},
            "Marylebone station": {"price": 200, "mortgage": 100, "mortgaged": False, "owned": False, "house_price": None, "hotel_price": None},
            "Bow Street": {"price": 180, "mortgage": 90, "mortgaged": False, "owned": False, "house_price": 100, "hotel_price": 500},
            "Marlborough Street": {"price": 180, "mortgage": 90, "mortgaged": False, "owned": False, "house_price": 100, "hotel_price": 500},
            "Vine Street": {"price": 200, "mortgage": 100, "mortgaged": False, "owned": False, "house_price": 100, "hotel_price": 500},
            "The Strand": {"price": 220, "mortgage": 110, "mortgaged": False, "owned": False, "house_price": 150, "hotel_price": 750},
            "Fleet Street": {"price": 220, "mortgage": 110, "mortgaged": False, "owned": False, "house_price": 150, "hotel_price": 750},
            "Trafalgar Square": {"price": 240, "mortgage": 120, "mortgaged": False, "owned": False, "house_price": 150, "hotel_price": 750},
            "Fenchurch Street station": {"price": 200, "mortgage": 100, "mortgaged": False, "owned": False, "house_price": None, "hotel_price": None},
            "Leicester Square": {"price": 260, "mortgage": 130, "mortgaged": False, "owned": False, "house_price": 150, "hotel_price": 750},
            "Coventry Street": {"price": 260, "mortgage": 130, "mortgaged": False, "owned": False, "house_price": 150, "hotel_price": 750},
            "Water Works": {"price": 150, "mortgage": "75", "mortgaged": False, "owned": False, "house_price": None, "hotel_price": None},
            "Piccadilly": {"price": 280, "mortgage": 140, "mortgaged": False, "owned": False, "house_price": 150, "hotel_price": 750},
            "Regent Street": {"price": 300, "mortgage": 150, "mortgaged": False, "owned": False, "house_price": 200, "hotel_price": 1000},
            "Oxford Street": {"price": 300, "mortgage": 150, "mortgaged": False, "owned": False, "house_price": 200, "hotel_price": 1000},
            "Bond Street": {"price": 320, "mortgage": 160, "mortgaged": False, "owned": False,"house_price": 200, "hotel_price": 1000},
            "Liverpool Street station": {"price": 200, "mortgage": 100, "mortgaged": False, "owned": False, "house_price": None, "hotel_price": None},
            "Park Lane": {"price": 350, "mortgage": 175, "mortgaged": False, "owned": False, "house_price": 200, "hotel_price": 1000},
            "Mayfair": {"price": 400, "mortgage": 200, "mortgaged": False, "owned": False, "house_price": 200, "hotel_price": 1000}
            }
        self.chance = {
            "Advance to Go (Collect £200)",
            "Advance to Trafalgar Square. If you pass Go, collect £200",
            "Advance to Mayfair",
            "Advance to Pall Mall. If you pass Go, collect £200",
            "Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
            "Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
            "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.",
            "Bank pays you dividend of £50",
            "Get Out of Jail Free",
            "Go Back 3 Spaces",
            "Go to Jail. Go directly to Jail, do not pass Go, do not collect £200",
            "Make general repairs on all your property. For each house pay £25. For each hotel pay £100",
            "Speeding fine £15",
            "Take a trip to Kings Cross Station. If you pass Go, collect £200",
            "You have been elected Chairman of the Board. Pay each player £50",
            "Your building loan matures. Collect £150"
        }
        self.community = {
            "Advance to Go (Collect £200)",
            "Bank error in your favour. Collect £200",
            "Doctor’s fee. Pay £50",
            "From sale of stock you get £50",
            "Get Out of Jail Free",
            "Go to Jail. Go directly to jail, do not pass Go, do not collect £200",
            "Holiday fund matures. Receive £100",
            "Income tax refund. Collect £20",
            "It is your birthday. Collect £10 from every player",
            "Life insurance matures. Collect £100",
            "Pay hospital fees of £100",
            "Pay school fees of £50",
            "Receive £25 consultancy fee",
            "You are assessed for street repairs. £40 per house. £115 per hotel",
            "You have won second prize in a beauty contest. Collect £10",
            "You inherit £100"
        }
        
    def HotelNumberChange(self, number):
        if self.hotels > number:
            self.hotels -= number
            return True
        else:
            return False
    def HousesNumberChange(self, number):
        if self.houses > number:
            self.houses -= number
            return True
        else:
            return False
    def AddParkFreeMoney(self, moneyOwed, playerMoney):
        self.parkFreeMoney += moneyOwed
        playerMoney -= moneyOwed
        return playerMoney
        
    def RemoveParkFreeMoney(self, playerMoney):
        playerMoney += self.parkFreeMoney
        self.parkFreeMoney = 0
        return playerMoney
    
    def PassGo(self, playerMoney):
        if self.bank > self.passGoMoney:
            self.bank -= self.passGoMoney
            playerMoney += self.passGoMoney
            return playerMoney
        else:
            return False
        
    def Tax(self, playerMoney):
        if playerMoney > self.tax:
            playerMoney -= self.tax
            self.bank += self.tax
            return playerMoney
        else:
            return False
        
    def SuperTax(self, playerMoney):
        if playerMoney > self.super_tax:
            playerMoney -= self.super_tax
            self.bank += self.super_tax
            return playerMoney
        else:
            return False
        
    def ChanceCard(self):
        chanceCard = random.choice(self.chance)
        return chanceCard
    
    def CommunityCard(self):
        communityChestCard = random.choice(self.community)
        return communityChestCard
    
    def LandOnProperty(self, playerMoney, propertyName, rent):
        if self.properties[propertyName]["owned"] != True:
            if playerMoney > self.properties[propertyName]["price"]:
                self.bank += self.properties[propertyName]["price"]
                playerMoney -= self.properties[propertyName]["price"]
                self.properties[propertyName]["owned"] = True
        else:
            if self.properties[propertyName]["mortgaged"] != True:
                playerMoney -= rent
        return playerMoney
                        
    def AuctionProperty(self):
        pass
    
    def MortageProperty(self, propertyName, playerMoney):
        if self.properties[propertyName]["mortgaged"] != True:
            self.properties[propertyName]["mortgaged"] = True
            playerMoney += self.properties[propertyName]["mortgage"]
        
    def UnMortgageProperty(self, propertyName, playerMoney):
        if self.properties[propertyName]["mortgaged"] == True:
            if playerMoney > self.properties[propertyName]["price"] * 1.1:
                playerMoney -= self.properties[propertyName]["price"] * 1.1
                self.properties[propertyName]["mortgaged"] == False
                
        return playerMoney
    
    def InJail(self, playerPosition, inJail):
        if self.board["Go To Jail"]["board_position"] == playerPosition:
            inJail = True
        else:
            inJail = False
        return inJail
    
    def Roll(self, playerPosition, inJail):
        if not inJail:
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            newPos = die1 + die2
            if playerPosition + newPos > 39:
                tempPos = playerPosition + newPos
                tempPos -= 40 # -39 position -1
                playerPosition = tempPos
                ##Then go to back to 0. that make be hard.
            else:
                playerPosition += newPos
                
            return playerPosition
        

class Player(object):
    def __init__(self, username, token, money=1500):
        self.money = money
        self.inJail = False
        self.playerTurn = False
        self.houses = 0
        self.hotels = 0
        self.properties = 0
        self.sets = 0
        self.username = username
        self.token = token
    def BuyProperty(self, propertyCost, propertyName, propertyColour, propertyBoardArea):
        if self.money > propertyCost:
            self.money -= propertyCost
            self.properties += 1
    def draw(self, win, positionX, positionY):
        win.blit(self.token, (positionX,positionY))
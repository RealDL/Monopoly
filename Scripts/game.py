import random, pygame, sys
from pygame import gfxdraw

class Setup(object):
    def __init__(self):
        self.startScreen = True
        self.setUp = False
        self.notSameUsername = False
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
        self.game = None
        self.players = []
        self.tokens = ["Images/Tokens/car.png","Images/Tokens/dog.png","Images/Tokens/hat.png","Images/Tokens/iron.png","Images/Tokens/ship.png","Images/Tokens/shoe.png","Images/Tokens/thimble.png","Images/Tokens/wheel.png"]
    def AddPlayers(self):
        if self.NumberOfPlayers < 6:
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
    def decreaseImageInterval(self):
        if self.imageInterval > 0:
            self.imageInterval -= 1
        else:
            self.imageInterval = len(self.tokens)-1
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
            "Advance to Go (Collect $200)",
            "Advance to Trafalgar Square. If you pass Go, collect $200",
            "Advance to Mayfair",
            "Advance to Pall Mall. If you pass Go, collect $200",
            "Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
            "Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
            "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.",
            "Bank pays you dividend of $50",
            "Get Out of Jail Free",
            "Go Back 3 Spaces",
            "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200",
            "Make general repairs on all your property. For each house pay $25. For each hotel pay $100",
            "Speeding fine $15",
            "Take a trip to Kings Cross Station. If you pass Go, collect $200",
            "You have been elected Chairman of the Board. Pay each player $50",
            "Your building loan matures. Collect $150"
        }
        self.community = {
            "Advance to Go (Collect $200)",
            "Bank error in your favour. Collect $200",
            "Doctor’s fee. Pay $50",
            "From sale of stock you get $50",
            "Get Out of Jail Free",
            "Go to Jail. Go directly to jail, do not pass Go, do not collect $200",
            "Holiday fund matures. Receive $100",
            "Income tax refund. Collect $20",
            "It is your birthday. Collect $10 from every player",
            "Life insurance matures. Collect $100",
            "Pay hospital fees of $100",
            "Pay school fees of $50",
            "Receive $25 consultancy fee",
            "You are assessed for street repairs. $40 per house. $115 per hotel",
            "You have won second prize in a beauty contest. Collect $10",
            "You inherit $100"
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
    """def AddParkFreeMoney(self, moneyOwed, playerMoney):
        self.parkFreeMoney += moneyOwed
        playerMoney -= moneyOwed
        return playerMoney
        
    def RemoveParkFreeMoney(self, playerMoney):
        playerMoney += self.parkFreeMoney
        self.parkFreeMoney = 0
        return playerMoney"""
    
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
    
    def PayOtherTax(self, playerMoney, tax):
        if playerMoney > tax:
            playerMoney -= tax
            self.bank += tax
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
                        
    def AuctionProperty(self, playerMoney, auctionPrice, newPlayerAuction):
        if playerMoney > auctionPrice:
            auctionPrice = newPlayerAuction
            return auctionPrice
        else:
            return False
        
    def WonAuction(self, playerMoney, auctionPrice):
        if playerMoney > auctionPrice:
            playerMoney -= auctionPrice
            self.bank += auctionPrice
            return playerMoney
        else:
            return False
    
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

class Player(object):
    def __init__(self, username, token, players, money=1500):
        self.money = money
        self.givePlayerMoney = False
        self.recieveMoneyFromPlayers = False
        self.players = players
        self.inJail = False
        self.playerTurn = False
        self.houses = 0
        self.hotels = 0
        self.position = 0
        self.positions = {
            0: {'x': 1376, 'y': 953}, 1: {'x': 1264, 'y': 953}, 2: {'x': 1181, 'y': 953}, 3: {'x': 1097, 'y': 953}, 
            4: {'x': 1013, 'y': 953}, 5: {'x': 929, 'y': 953}, 6: {'x': 843.5, 'y': 953}, 7: {'x': 759.5, 'y': 953},
            8: {'x': 675.5, 'y': 953}, 9: {'x': 591.5, 'y': 953}, 10: {'x': 482, 'y': 953}, 11: {'x':482, 'y': 847}, 
            12: {'x':482, 'y': 763}, 13: {'x':482, 'y': 679}, 14: {'x':482, 'y': 594}, 15: {'x':482, 'y': 509}, 
            16: {'x':482, 'y': 424}, 17: {'x':482, 'y': 340}, 18: {'x':482, 'y': 255}, 19: {'x': 482, 'y': 171}, 
            20: {'x': 482, 'y': 60}, 21: {'x': 591.5, 'y': 60}, 22: {'x': 675.5, 'y': 60}, 23: {'x': 759.5, 'y': 60}, 
            24: {'x': 843.5, 'y': 60}, 25: {'x': 929, 'y': 60}, 26: {'x': 1013, 'y': 60}, 27: {'x': 1097, 'y': 60}, 
            28: {'x': 1181, 'y': 60}, 29: {'x': 1264, 'y': 60}, 30: {'x': 1376, 'y': 60}, 31: {'x': 1376, 'y': 171}, 
            32: {'x': 1376, 'y': 255}, 33: {'x': 1376, 'y': 340}, 34: {'x': 1376, 'y': 424}, 35: {'x': 1376, 'y': 509}, 
            36: {'x': 1376, 'y': 594}, 37: {'x': 1376, 'y': 679}, 38: {'x': 1376, 'y': 763}, 39: {'x': 1376, 'y': 847}
        }
        self.chance = {
            0:"Advance to Go (Collect $200)",
            1:"Advance to Trafalgar Square. If you pass Go, collect $200",
            2:"Advance to Mayfair",
            3:"Advance to Pall Mall. If you pass Go, collect $200",
            4:"Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
            5:"Advance to the nearest Station. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled",
            6:"Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.",
            7:"Bank pays you dividend of $50",
            8:"Get Out of Jail Free",
            9:"Go Back 3 Spaces",
            10:"Go to Jail. Go directly to Jail, do not pass Go, do not collect $200",
            11:"Make general repairs on all your property. For each house pay $25. For each hotel pay $100",
            12:"Speeding fine $15",
            13:"Take a trip to Kings Cross Station. If you pass Go, collect $200",
            14:"You have been elected Chairman of the Board. Pay each player $50",
            15:"Your building loan matures. Collect $150"
        }
        self.community = {
            0:"Advance to Go (Collect $200)",
            1:"Bank error in your favour. Collect $200",
            2:"Doctor's fee. Pay $50",
            3:"From sale of stock you get $50",
            4:"Get Out of Jail Free",
            5:"Holiday fund matures. Receive $100",
            6:"Go to Jail. Go directly to jail, do not pass Go, do not collect $200",
            7:"Income tax refund. Collect $20",
            8:"It is your birthday. Collect $10 from every player",
            9:"Life insurance matures. Collect $100",
            10:"Pay hospital fees of $100",
            11:"Pay school fees of $50",
            12:"Receive $25 consultancy fee",
            13:"You are assessed for street repairs. $40 per house. $115 per hotel",
            14:"You have won second prize in a beauty contest. Collect $10",
            15:"You inherit $100"
        }
        self.properties = []
        self.sets = 0
        self.username = username
        self.token = token
        self.x = self.positions[self.position]["x"]
        self.y = self.positions[self.position]["y"]
        self.load_image = pygame.image.load(self.token).convert()
        self.networth = 1500
        self.double = False
        self.doubleCount = 0
        self.passedGo = False
        self.salary = 200
        self.getOutOfJailCost = 50
        self.GoesInJail = 0
        self.income_tax = 200
        self.super_tax = 100
        self.title = ""
        self.information = ""
        self.displayEvent = False
        self.reason = ""
        self.getOutOfJailCard = 0
    """def BuyProperty(self, propertyCost, property):
        if self.money > propertyCost:
            self.money -= propertyCost
            self.properties.append(property)"""
            
    """def OutOfGame(self, debt):
        if self.networth < debt:
            self.networth = 0
            return True
        else:
            return False"""
            
    def draw(self, win, positionX, positionY):
        win.blit(self.load_image, (positionX,positionY))

    def screen(self, win):
        # create a rounded rectangle surface
        rect_width, rect_height = self.load_image.get_width() // 2, self.load_image.get_height() // 2
        corner_radius = 5
        rounded_rect = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
        pygame.draw.rect(rounded_rect, (250, 250, 250, 150), (0, 0, rect_width, rect_height), border_radius=corner_radius)

        # scale the image
        scaled_image = pygame.transform.scale(self.load_image, (rect_width - corner_radius*2, rect_height - corner_radius*2))

        # get the position of the rounded rectangle
        self.x = self.positions[self.position]["x"]
        self.y = self.positions[self.position]["y"]
    
        # blit the image onto the rounded rectangle
        win.blit(rounded_rect, (self.x, self.y))
        win.blit(scaled_image, (self.x + corner_radius, self.y + corner_radius))
    
    ## Character Movements etc
    def Double(self, num1, num2):
        if num1 == num2:
            self.double = True
            self.doubleCount += 1
            self.displayEvent = True
            self.title = self.username + ", you rolled two " + str(num1) + "s!"
            self.information = "Becuase you rolled a double, you get to have another go."
        else:
            self.double = False
            self.doubleCount = 0
            self.displayEvent = True
            self.title = self.username + ", you rolled a " + str(num1) + " and a " + str(num2) + "!"
            self.information = "Your turn will end here."
            
    def MoveCharacter(self, newPos):
        if self.position + newPos > 39:
            tempPos = self.position + newPos
            tempPos -= 40 # -39 position -1
            self.position = tempPos
            self.passedGo = True
            self.displayEvent = True
            self.title = self.username +", you passed Go!"
            self.information = "You earnt $200 because you passed go."
            ##Then go to back to 0. that make be hard.
        else:
            self.position += newPos
        
    def Tax(self):
        if self.position == 4:
            if self.money > self.income_tax:
                self.money -= self.income_tax
                self.networth -= self.income_tax
            self.displayEvent = True
            self.title = self.username + ", you landed on income tax!"
            self.information = "You were forced to pay $200 to the bank!"
                    
        if self.position == 38:
            if self.money > self.super_tax:
                self.money -= self.super_tax
                self.networth -= self.super_tax 
            self.displayEvent = True
            self.title = self.username + ", you landed on super tax!"
            self.information = "You were forced to pay $100 to the bank!"
        
    def ChanceCard(self):
        if self.position == 7 or self.position == 22 or self.position == 36:
            randomChance = random.randint(0,15)
            yourChanceCARD = self.chance[randomChance]
            self.displayEvent = True
            self.title = self.username + ", you landed on chance!"
            self.information = str(yourChanceCARD)
            if randomChance == 0:
                self.passedGo = True
                self.position = 0
            elif randomChance == 1:
                if self.position > 24:
                    self.passedGo = True
                self.position = 24
            elif randomChance == 2:
                self.position = 39
            elif randomChance == 3:
                if self.position > 11:
                    self.passedGo = True
                self.position = 11
            elif randomChance == 4 or randomChance == 5:
                if self.position < 5:
                    self.position = 5
                elif self.position > 35:
                    self.position = 5
                    self.passedGo = True
                elif self.position < 15 and self.position > 5:
                    self.position = 15
                elif self.position < 25 and self.position > 15:
                    self.position = 25
                elif self.position < 35 and self.position > 25:
                    self.position = 35
            elif randomChance == 6:
                if self.position < 12:
                    self.position = 12
                elif self.position > 24:
                    self.position = 12
                    self.passedGo = True
                elif self.position > 12 and self.position < 24:
                    self.position = 24
            elif randomChance == 7:
                self.money += 50
                self.networth += 50
            elif randomChance == 8:
                self.getOutOfJailCard += 1
            elif randomChance == 9:
                self.position -= 3
            elif randomChance == 10:
                self.inJail = True
            elif randomChance == 11:
                cost = self.hotels * 100 + self.houses *25
                if self.money > cost:
                    self.money -= cost
                    self.networth -= cost
            elif randomChance == 12:
                cost = 15
                if self.money > cost:
                    self.money -= cost
                    self.networth -= cost
            elif randomChance == 13:
                if self.position > 5:
                    self.passedGo = True
                self.position = 5
            elif randomChance == 14:
                cost = self.players * 50
                if self.money > cost:
                    self.money -= cost
                    self.networth -= cost
                    self.givePlayerMoney = True
            elif randomChance == 15:
                money = 150
                self.money += money
                self.networth += money
            
            #12 - 15 of chance then community chest.
                        
            print(yourChanceCARD)
        
    def CommunityChestCard(self):
        if self.position == 2 or self.position == 17 or self.position == 33:
            randomCommunity = random.randint(0,15)
            yourCommunityChestCARD = self.community[randomCommunity]
            self.displayEvent = True
            self.title = self.username + ", you landed on community chest!"
            self.information = str(yourCommunityChestCARD)
            print(yourCommunityChestCARD)
            
            if randomCommunity == 0:
                self.passedGo = True
                self.position = 0
            elif randomCommunity == 1:
                self.money += 200
                self.networth += 200
            elif randomCommunity == 2:
                self.money -= 50
                self.networth -= 50
            elif randomCommunity == 3:
                self.money += 50
                self.networth += 50
            elif randomCommunity == 4:
                self.getOutOfJailCard += 1
            elif randomCommunity == 5:
                self.money += 100
                self.networth += 100
            elif randomCommunity == 6:
                self.inJail = True
            elif randomCommunity == 7:
                self.money += 20
                self.networth += 20
            elif randomCommunity == 8:
                money = self.players * 10
                self.money += money
                self.networth += money
                self.recieveMoneyFromPlayers = True
            elif randomCommunity == 9:
                self.money += 100
                self.networth += 100
            elif randomCommunity == 10:
                self.money -= 100
                self.networth -= 100
            elif randomCommunity == 11:
                self.money -= 50
                self.networth -= 50
            elif randomCommunity == 12:
                self.money += 25
                self.networth += 25
            elif randomCommunity == 13:
                cost = self.houses * 40 + self.hotels * 115
                if self.money > cost:
                    self.money -= cost
                    self.networth -= cost
            elif randomCommunity == 14:
                self.money += 10
                self.networth += 10
            elif randomCommunity == 15:
                self.money += 100
                self.networth += 100
                    
    def GoToJail(self):
        if self.doubleCount >= 3:
            self.reason = "you rolled 3 doubles in a row!"
            self.inJail = True
        if self.position == 30:
            self.reason = "you landed on go to jail!"
            self.inJail = True
        
    def AreYouInJail(self):
        if self.inJail:
            self.double = False
            self.position = 10
            self.passedGo = False
            self.doubleCount = 0
            self.displayEvent = True
            self.title = self.username + ", your in Jail!"
            self.information = "You are in Jail because " + self.reason
              
    def PassedGo(self):
        if self.passedGo:
            self.money += self.salary
            self.networth += self.salary
            self.passedGo = False    
          
    def PlayerGetOutOfJail(self):
        die1, die2 = random.randint(1,6), random.randint(1,6)
        newPos = die1 + die2
        print(die1, die2)
        if self.getOutOfJailCard < 1:
            if self.GoesInJail <= 3:
                if die1 == die2:
                    self.double = True
                    self.doubleCount += 1
                    self.inJail = False
                    self.position += newPos
                    self.displayEvent = True
                    self.title = self.username + ", you rolled two " + str(die1) + "s. You're free!"
                    self.information = "You are now free from Jail!"
                else:
                    self.displayEvent = True
                    self.title = self.username + ", you rolled a " + str(die1) + " and a " + str(die2) + "!"
                    self.information = "You failed to get a double. Try again next time!"
            else:
                self.GetOutOfJail()
        else:
            self.getOutOfJailCard -= 1
            self.inJail = False
            self.position += newPos
            self.displayEvent = True
            self.title = self.username + ", you used your get out of jail card!"
            self.information = "You are now free from Jail!"
            
             
    def Roll(self):
        if self.playerTurn != True:
            if self.inJail != True:
                die1, die2 = random.randint(1,6), random.randint(1,6)
                print(die1, die2)
                newPos = die1 + die2
                self.Double(die1, die2)
                self.MoveCharacter(newPos)
                self.Tax()
                self.ChanceCard()
                self.CommunityChestCard()
                self.GoToJail()
                self.AreYouInJail()
                self.PassedGo()
             
            if self.inJail:
                self.GoesInJail += 1
                if self.GoesInJail >= 1 and self.double == True:
                    self.PlayerGetOutOfJail()
            if self.double != True:
                self.playerTurn = True

    def EndTurn(self):
        self.playerTurn = False

    def GetOutOfJail(self):
        if self.inJail and self.playerTurn != True:
            if self.money > self.getOutOfJailCost:
                self.displayEvent = True
                self.title = "You paid $50 to get out of Jail!"
                self.information = "You are now free from Jail!"
                self.money -= self.getOutOfJailCost
                self.networth -= self.getOutOfJailCost
                self.inJail = False
                self.Roll()


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
        ## self.click = False
        ## self.hover = False
    def BuyProperty(self, propertyCost, propertyName, propertyColour, propertyBoardArea):
        if self.money > propertyCost:
            self.money -= propertyCost
            self.properties += 1
    
        
        
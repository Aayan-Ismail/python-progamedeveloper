class Player:
    def __init__(self, username, level):
        self.username = username
        self.level = level
    
    def display_player(self):
        print("Username:", self.username)
        print("Level:", self.level)

class GamingProfile(Player):
    def __init__(self, username, level, andrew_coins):
        super().__init__(username,level)
        self.andrew_coins = andrew_coins
    
    def buy_item(self, price):
        if self.andrew_coins >= price:
            self.coins -= price
            print("Item purchased!")    
            print("Remaining Andrew Coins", self.coins)
        else:
            print("Not enough Andrew Coins")

player = GamingProfile("stanleyishmael", 116,5)

player.display_player()

print()

player.buy_item(300)
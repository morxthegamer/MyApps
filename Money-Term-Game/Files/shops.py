class Shops:
    def __init__(self):
        self.shopList = [

        ]

        self.money = None

    @property
    def getMoney(self):
        with open("Data/money.yaml", "r") as g:
            self.money = g.read()[10]
            print(self.money)
            return self.money

    def writeMoney(self, money):
        with open("Data/money.yaml", "w") as f: f.write("[MONEY]: {}".format(money))

    def spend(self):
        pass
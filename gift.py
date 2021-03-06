class Gift():
    """Gift factory to create a gift to go into a wishlist"""
    __count = 0

    @staticmethod
    def tracking():
        print("Total gifts: " + str(Gift.__count) + "\n")

    def __init__(self, name, cost, color = None):
        self.__name = name
        self.__cost = cost
        self.__color = color
        self.__purchased = False
        Gift.__count += 1

    def __str__(self):
        reply = self.__name
        return reply

    def purchase(self):
        self.__purchased = True

    def is_purchased(self):
        return self.__purchased
    def get_price(self):
        return self.__cost
    def get_name(self):
        return self.__name

if __name__ == "__main__":
    Gift.tracking()
    gift1 = Gift("Toy Airplane", 10, "red" )
    print(gift1)
    print(gift1.is_purchased())
    gift2 = Gift("Lego Set", 25 )
    gift2.purchase() 
    print(gift2)
    print(isinstance(gift2,Gift)) 
    Gift.tracking()

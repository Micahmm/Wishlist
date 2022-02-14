import people, data_handling, gift
from gift import Gift
from people import Person
from data_handling import table_print

class WishList:
    ##keeps track of the list id
    __list_id = 1
    ##list of wishlists
    __total_list = []

    

    
    def __init__(self,person,address):
        self.__person = person
        self.__gift_list = []
        self.__delivery = False
        self.__address = address
        self.__list_id = WishList.__list_id
        WishList.__list_id += 1
        WishList.__total_list.append(self)
    ##Helped by Siddharth Patwardhan in office hours
    ##method to add gift
    def addGift(self,gift):
        if isinstance(gift,Gift) and gift not in self.__gift_list and not self.__delivery:
            self.__gift_list.append(gift)
    ##Helped by Manita Pote in office hours
    ##method to remove gift
    def removeGift(self,gift):
        if gift in self.__gift_list:
            self.__gift_list.remove(gift)
    ##method to purchase gift                
    def purchase(self):
        if not self.__delivery:
            self.delivery = True
    ##Helped by Manita Pote in office hours
    ##method to display the wishlist
    def display_list(self):
        table = {}
        print("Wishlist Name:",self.__person.get_name())
        for gift in self.__gift_list:
            table[gift.get_name()] = gift.get_price()
        table_print(["Gift", "Price"], list(table.items()), 20)

    
    ##Helped by Hannah Hasenwinkel in office hours
    ##method to display the most popular gift
    @staticmethod
    def popular():
        max_num = 0
        pop_list = []
        for item in WishList.__total_list:
            for gift in item.get_list():
                pop_list.append(str(gift))
        for gift in pop_list:
            gift_count = pop_list.count(gift)
            if gift_count > max_num:
                max_num = gift_count
                pop_gift = gift
        print("Most popular gift:",gift,",with a quantity of",max_num)
    ##Helped by Will Bankston in office hours
    ##method to display all gifts within a specified state
    @staticmethod
    def state(state):
        gifts = {}
        for item in WishList.__total_list:
            if not item.__delivery and item.__address.split(",")[1] == state:
                for gift in item.get_list():
                    if str(gift) not in gifts:
                        gifts[str(gift)] = 1
                    else:
                        gifts[str(gift)] += 1
        data_handling.table_print(["Gift", "Quantity"], gifts.items(), 20)
        

        
                
    ##getter for state method
    def get_list(self):
        return self.__gift_list
          
            
            

##main of code and used for testing and actaully inputting data
if __name__ == "__main__":
    child1 = Person("Jim", "jim@aol.com")
    child2 = Person("Bob","bob@gmail.com")
    child3 = Person("Timmy","tim@aol.com")
    child4 = Person("Tom","tom@aol.com")
    child5 = Person("Sam","sam@gmail.com")

    gift1 = Gift("Toy Car",15)
    gift2 = Gift("Watch", 200)
    gift3 = Gift("Toy Plane", 20)
    gift4 = Gift("Legos", 8)
    gift5 = Gift("Ball", 5)
    gift6 = Gift("Tent", 85)
    gift7 = Gift("IPad", 400)
    gift8 = Gift("Xbox", 210)

    W1 = WishList(child1,"Indianapolis,IN")

    W1.addGift(gift1)
    W1.addGift(gift2)
    W1.popular()
    W1.display_list()

    W2 = WishList(child2,"San Fransisco, California")
    W2.addGift(gift3)
    W2.display_list()

    W3 = WishList(child3,"New York, NY")
    W3.addGift(gift4)
    W3.addGift(gift3)
    W3.removeGift(gift3)
    W3.purchase()
    W3.display_list()

    W4 = WishList(child4,"Gary, IN")
    W4.addGift(gift4)
    W4.addGift(gift5)
    W4.addGift(gift6)
    W4.addGift(gift7)
    W4.display_list()

    
    W5 = WishList(child3,"Austin, TX")
    W5.addGift(gift4)
    W5.display_list()

    
  

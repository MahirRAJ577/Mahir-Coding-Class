class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")
    
    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()
print()

print("try to update maxprice directly")
c.__maxprice = 750
c.sell()

print("after using the method setMaxPrice:")
c.setMaxPrice(1000)
c.sell()
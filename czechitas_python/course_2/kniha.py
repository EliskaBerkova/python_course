class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self. pages = pages
        self.price = price
    def discount(self, discount):
        self.price = self.price - (self.price/ 100 * discount)
    
    def getInfo(self):
        print(f"Kniha {self.title} ma {self.pages} stran a stoji {self.price} Kc.")

nazapade = Book("Na zapadni fronte klid", 354, 299)
nazapade.getInfo()
nazapade.discount(25)
nazapade.getInfo()


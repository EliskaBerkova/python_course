class Package:
    def __init__(self, address, weightInKilos):
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False
    def deliver(self):
        self.delivered = True

    def getInfo(self):
        print(f"Balik na adresu: {self.address}, vaha: {self.weightInKilos} kg.")
        if self.delivered == False:
            print ("Balik zatim nebyl dorucen.")
        else:
            print("Balik byl dorucen.")

class ValuablePackage(Package):
    def __init__(self, address, weightInKilos, value):
        super().__init__(address, weightInKilos)
        self.value = value
    def getInfo(self):
        super().getInfo()
        print(f"Hodnota baliku je {self.value} Kc.")


balik = Package("Opava", 12)
balik.getInfo()
balik.deliver()
balik.getInfo()

hodnotnyBalik = ValuablePackage("Kravare", 2.5, 250)
hodnotnyBalik.getInfo()


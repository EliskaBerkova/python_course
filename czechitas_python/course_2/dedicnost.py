class Employee:
    def takeHoliday (self, days):
        if self.holidays >= days:
            self.holidays -= days
            print("Dovolena odectena")
        else:
            print("Na tolik dni nemas narok.")
    def getName (self):
        return self.name
    def getInfo(self):
        print(f"{self.name} pracuje na pozici {self.position}.")

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.holidays = 25
        

class Manager(Employee):
    def getInfo(self):
        super().getInfo()
        print(f"Ma {self.sub} podrizenych.")
    def __init__(self, name, position, sub):
        super().__init__(name, position)
        self.sub = sub


frantisek = Employee("František Novák", "konstruktér")
frantisek.getInfo()

klara = Employee("Klára Nová", "konstruktérka")
klara.getInfo()

ivan = Employee("Ivan Horký", "skladník")
ivan.getInfo()

boss = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 2)
boss.getInfo()
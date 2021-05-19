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
        if self.probation == True:
            print("Je ve zkusebni dobe.")
        else:
            print("Neni ve zkusebni dobe.")
    def __init__(self, name, position, probation):
        self.name = name
        self.position = position
        self.holidays = 25
        self.probation = probation


frantisek = Employee("František Novák", "konstruktér", True)
frantisek.getInfo()
frantisek.takeHoliday(5)
frantisek.takeHoliday(15)
frantisek.takeHoliday(5)
frantisek.takeHoliday(4)

klara = Employee("Klára Nová", "konstruktérka", False)
klara.getInfo()

ivan = Employee("Ivan Horký", "skladník", False)
ivan.getInfo()

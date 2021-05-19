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


class PartTimeEmployee(Employee):
    def __init__(self, name, position, workload):
        super().__init__(name, position)
        self.workload = workload
    def getInfo(self):
        super().getInfo()
        print(f"Uvazek je {self.workload}")

frantisek = Employee("František Novák", "konstruktér")
frantisek.getInfo()
frantisek.takeHoliday(5)

klara = Employee("Klára Nová", "konstruktérka")
klara.getInfo()

ivan = PartTimeEmployee("Ivan Horký", "skladník", 0.5)
ivan.getInfo()

print(ivan.name)
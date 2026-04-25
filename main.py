# 1
class CarFuel:
    def __init__(self, model, fuel):
        self.model = model
        self.fuel = fuel

    def drive(self):
        return f"{self.model}  km yurildi, "

    def refuel(self):
        return f" Yoqilg‘i to‘ldirildi: {self.fuel}, "

student1 = CarFuel(10, input("kirit : "))
print(student1.drive())
print(student1.refuel())



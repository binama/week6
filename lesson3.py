class Car:
    wheels = 4
    def __init__(self, model, color, owner, year):
        self.model = model
        self.miles = 0
        self.fuel = 0
        self.color = color
        self.owner = owner
        self.year = year
    def get_fuel(self, litr ):
        self.fuel += litr
        print(f"Вы залили {litr} литров бензина, итого {self.fuel} литров у вас в баке")
        return self.fuel
    def drive(self, km):
        litr = km * 0.1
        if self.fuel >= litr:
            print("Мы смело едем!!!")
            self.miles += km
            self.fuel -= litr
        else:
            print("У вас недостаточно бензина!!!")
    def change_color(self, new_color):
        self.color = new_color
        print(f"Позлравляю с новым цветом машины! {self.color}")
tesla = Car("Model X", "white", "Nazgul", "2022")
tesla.change_color("green")
porshe = Car("Cayenne", "red", "Mirlan", "2022")
porshe.exous = "noise"
print(tesla.__dict__)
print(porshe.__dict__)
tesla.get_fuel(40)
tesla.get_fuel(50)
porshe.get_fuel(50)
tesla.drive(400)
porshe.drive(800)
tesla.wheels = 6
print(tesla.wheels)
print(porshe.wheels)
print(tesla.__dict__)      #метод дикт показывает только его значение
print(porshe.__dict__)
del tesla.wheels
print()
print(tesla.__dict__)      #метод дикт показывает только его значение
print(porshe.__dict__)
print(tesla.fuel)
print(tesla.color)
print(porshe.fuel)
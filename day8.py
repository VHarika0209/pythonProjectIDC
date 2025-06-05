class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"Car Details:")
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year  : {self.year}")
        print(f"Color : {self.color}")

# Creating objects
car1 = Car("Toyota", "Camry", 2020, "Blue")
car2 = Car("Tesla", "Model 3", 2023, "White")

# Displaying info
car1.display_info()
# print()
car2.display_info()

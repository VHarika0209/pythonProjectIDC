# Import the Car Class from day8.py
from day8 import Car

# Child class extending Car
class ElectricCar(Car):
    def __init__(self,brand,model,year,color,battery_capacity):
        super().__init__(brand, model, year, color)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity :{self.battery_capacity}")

# Create an ElectricCar instance
my_ev = ElectricCar("Tata", "Nexon EV",2025,"Teal Blue",40)
my_ev.display_info()

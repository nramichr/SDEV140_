"""

2. Car ClassWrite a class named Car that has the following data attributes: 

(for the car’s year model)
(for the make of the car)                             
(for the car’s current speed)

The Car class should have an method that accepts the car’s year model and make as arguments. 
These values should be assigned to the object’s and data attributes. It should also assign 0 to the data attribute.

The class should also have the following methods:

accelerate
The accelerate method should add 5 to the speed data attribute each time it is called.

brake
The brake method should subtract 5 from the speed data attribute each time it is called.

get_speed
The get_speed method should return the current speed.

Next, design a program that creates a  object then calls the accelerate method five times. 
After each call to the accelerate method, get the current speed of the car and display it. 
Then call the  method five times. After each call to the  method, get the current speed of the car and display it.

"""

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    def accelerate(self):
        self.__speed += 5
    def brake(self):
        self.__speed -= 5
    def get_speed(self):
        return self.__speed
    def get_year_model(self):
        return self.__year_model
    def get_make(self):
        return self.__make

def main():
    car = Car(1994, "Mercedes-Benz")

    print(f"Car: {car.get_year_model()} {car.get_make()}")
    print()

    print("Accelerating")
    for i in range(5):
        car.accelerate()
        print(f"Speed:{car.get_speed()}mph")

    print()
    print("Braking")
    for i in range(5):
        car.brake()
        print(f"Speed:{car.get_speed()}mph")

if __name__ == "__main__":
    main()
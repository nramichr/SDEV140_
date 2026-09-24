"""
Reference Chapter 11 programming problem 1 p606.

Write an Employee class that keeps data attributes for the following pieces of information:

Employee name
Employee Number

Next, write a class named ProductionWorker that is a subclass of the Employee class.  The ProductionWorker class should keep data attributes 

Shift Number (1 day or 2 night)
Hourly Pay Rate

Write appropriate Accessor and Mutator methods for each class. 

Once you have written the classes, write a program that creates an object of the ProductionWorker.  
Use the accessor methods to print out the object's full state.  
Then test the mutator methods doing an update of all attributes followed by a second print of the object's full revised state. 

"""

class Employee:

    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

class ProductionWorker(Employee):

    def __init__(self, name, number, shift, pay_rate):
        super().__init__(name, number)
        self.__shift = shift
        self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__pay_rate

    def get_pay_rate(self):
        return self.__pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

def shift_description(shift_number):

    if shift_number == 1:
        return "Day"
    elif shift_number == 2:
        return "Night"
    else:
        return "Unknown"

def print_worker_info(worker):
    print(f"Name {worker.get_name()}")
    print(f"Employee Numbder: {worker.get_number()}")
    print(f"Shift: {worker.get_shift()} ({shift_description(worker.get_shift ())})")
    print(f"Hourly Pay Rate: ${worker.get_pay_rate():.2f}")
    print()

def main():
    worker = ProductionWorker("Christian Ramirez-Flores", 4821, 1, 18.50)

    print("Original State")
    print_worker_info(worker)

    worker.set_name("Christian Ramirez-Flores")
    worker.set_number(4882)
    worker.set_shift(2)
    worker.set_pay_rate(21.75)

    print("Altered State")
    print_worker_info(worker)

if __name__ == "__main__":
    main()


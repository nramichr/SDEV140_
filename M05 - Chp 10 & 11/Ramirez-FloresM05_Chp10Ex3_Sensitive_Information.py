"""

3. Personal Information ClassDesign a class that holds the following personal data: name, address, age, and phone number. 
Write appropriate accessor and mutator methods. Also, write a program that creates three instances of the class. 
Each instance should hold fictional information for a fake person. (For privacy purposes, do not store real personal information in your program.)

"""

class PersonalInformation:
    def __init__(self, name, address, age, phone_number):
        self._name = name
        self._address = address
        self._age = age
        self._phone_number = phone_number

    def get_name(self):
        return self._name
    def get_address(self):
        return self._address
    def get_age(self):
        return self._age
    def get_phone_number(self):
        return self._phone_number

    def set_name(self, name):
        self._name = name
    def set_address(self, address):
        self._address = address
    def set_age(self, age):
        self._age = age
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number
def main():
    client1 = PersonalInformation("Max Verstappen", "1234 Terrace Ave, Minnesota", 42, "301-574-3632")
    client2 = PersonalInformation("Sandy Contreras","4589 Columbian Ave, Chicago", 30, "301-324-2390")
    client3 = PersonalInformation("Lewis Hamilton","21938 Corndance St, Miami", 35, "305-329-7892")

    people = [client1,client2,client3]

    for i, client in enumerate(people, 0): #Originally I'd placed a '1' for the starting list which caused an error but reviesd to '0'. 
        print()
        print("Client Data")
        print(f"Name: {client.get_name()}")
        print(f"Address: {client.get_address()}")
        print(f"Age: {client.get_age()}")
        print(f"Phone Number: {client.get_phone_number()}") #***FIXED*** if i place "get_phone_number" I get a "<bound method PersonalInformation.get_phone_number of <__main__.PersonalInformation object at 0x000002B0841D8690>>"
        print()

if __name__ == "__main__":
    main()
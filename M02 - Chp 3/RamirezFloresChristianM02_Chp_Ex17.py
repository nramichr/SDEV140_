"""
You have a group of friends coming to visit for your high school reunion, and you want to take them out to eat at a local restaurant.  
You aren’t sure if any of them have dietary restrictions, but your restaurant choices are as follows:

Joe’s Gourmet Burgers–Vegetarian: No, Vegan: No, Gluten-Free: No
Main Street Pizza Company–Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
Corner Café–Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
Mama’s Fine Italian–Vegetarian: Yes, Vegan: No, Gluten-Free: No
The Chef’s Kitchen–Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes

Write a program that asks whether any members of your party are vegetarian, vegan, or gluten-free, to which then displays 
only the restaurants to which you may take the group. 

"""
def main():
    vegetarians: str = input("Are any of your friends vegetarian? (y/n): ")
    vegans: str = input("Are any of your friends vegan? (y/n): ")
    gluten_free: str = input("Are any of your friends gluten-free? (y/n): ")


    print("Here are your restaurant choices:")
    if vegetarians == 'n' and vegans == 'n' and gluten_free == 'n':
        print("Joe's Gourmet Burgers")
        print("Main Street Pizza Company")
        print("Corner Café")
        print("Mama's Fine Italian")
        print("The Chef's Kitchen")
    elif vegetarians == 'y' and vegans == 'n' and gluten_free == 'n':
        print("Main Street Pizza Company")
        print("Corner Café")
        print("Mama's Fine Italian")
        print("The Chef's Kitchen")
    elif vegetarians == 'n' and vegans == 'y' and gluten_free == 'n':
        print("Corner Café")
        print("The Chef's Kitchen")
    elif vegetarians == 'n' and vegans == 'n' and gluten_free == 'y':
        print("Main Street Pizza Company")
        print("Corner Café")
        print("The Chef's Kitchen")
    elif vegetarians == 'y' and vegans == 'y' and gluten_free == 'y':
        print("Corner Café")
        print("The Chef's Kitchen")
    elif vegetarians == 'y' and vegans == 'y' and gluten_free == 'n':
        print("Corner Café")
        print("The Chef's Kitchen")
    elif vegetarians == 'y' and vegans == 'n' and gluten_free == 'y':
        print("Main Street Pizza Company")
        print("Corner Café")
        print("The Chef's Kitchen")
    elif vegetarians == 'n' and vegans == 'y' and gluten_free == 'y':
        print("Corner Café")
        print("The Chef's Kitchen")
main()

"""
    10.
    A cookie recipe calls for the following ingredients: 
    1.5 cups of sugar  1 cup of butter  2.75 cups of flour
    The recipe produces 48 cookies with this amount of the ingredients.
    Write a program that asks the user how many cookies he or she wants to make, 
    then displays the number of cups of each ingredient needed for the specified number of cookies.
"""

print("How many cookies would you like to make today?")
cookie_amount = int(input())
print("You want to make", cookie_amount, "cookies.")
decision = input("Is that correct? (y/n): ")
if decision.lower() == 'y':
    print("Great! Let's get started.")
else:
    print("Please restart the program and enter the correct amount of cookies.")
if decision.lower() == 'n':
 exit()
sugar_per_cookie = 1.5
butter_per_cookie = 1.0
flour_per_cookie = 2.75

sugar_amount_needed = sugar_per_cookie * cookie_amount
butter_amount_needed = butter_per_cookie * cookie_amount
flour_amount_needed = flour_per_cookie * cookie_amount

print("According to the maths this is how much you'll need to make", cookie_amount, "cookies:")
print("Cups of sugar needed:", sugar_amount_needed)
print("Cups of butter needed:", butter_amount_needed)
print("Cups of flour needed:", flour_amount_needed)
print("How many cookies would you like to make today?")
cookie_amount = int(input())
print("You want to make", cookie_amount, "cookies.")
y_o_n = input("Is that correct? (y/n): ")
if y_o_n.lower() == 'y':
    print("Great! Let's get started.")
else:
    print("Please restart the program and enter the correct amount of cookies.")
if y_o_n.lower() == 'n':
 exit()
sugar_per_cookie = 1.5
butter_per_cookie = 1.0
flour_per_cookie = 2.75
sugar_amount_needed = sugar_per_cookie * cookie_amount
butter_amount_needed = butter_per_cookie * cookie_amount
flour_amount_needed = flour_per_cookie * cookie_amount
print("According to the maths this is how much you'll need to make", cookie_amount, "cookies:")
print("Sugar needed:", sugar_amount_needed)
print("Butter needed:", butter_amount_needed)
print("Flour needed:", flour_amount_needed)
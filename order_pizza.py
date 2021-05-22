# Pizza order coding challenge
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, L ... ")
add_pepperoni = input("Do you want pepperoni? Y or N ... ")
extra_cheese = input("Do you want extra cheese? Y or N ... ")

if size == "S":
    small_pizza = 15
    if add_pepperoni == "Y":
        small_pizza += 2
    if extra_cheese == "Y":
        small_pizza += 1
    print(f"Your final bill is: ${small_pizza}.")
if size == "M":
    medium_pizza = 20
    if add_pepperoni == "Y":
        medium_pizza += 3
    if extra_cheese == "Y":
        medium_pizza += 1
    print(f"Your final bill is: ${medium_pizza}.")
if size == "L":
    large_pizza = 25
    if add_pepperoni == "Y":
        large_pizza += 3
    if extra_cheese == "Y":
        large_pizza += 1
    print(f"Your final bill is: ${large_pizza}.")

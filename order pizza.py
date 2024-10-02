# order pizza
# price of original pizza
price = 0

# welcome to pizza cuy!!!
print("#########################")
print("  WELCOME TO PIZZA CUY!")
print("#########################")

# what is the customer's name?
name = input("Customer Name = ")
date = input("Date = ")

# display topping
print("""\n============TOPPINGS============""")
print("1 |Original Pizza     |30,000 ")
print("2 |Beef BBQ Pizza     |65,000 ")
print("3 |Chicken Mayo Pizza |60,000 ")
print("4 |Pepperoni Pizza    |45,000 ")
print("5 |Tuna Mayo Pizza    |65,000 ")
print("""===============================""")
chosen_topping = input("Chosen Topping: ") 

# Check chosen topping and display the price
if chosen_topping == "original pizza":
    topping_price = 30000
    price += 30000
    print(f"Topping price: {topping_price}")
elif chosen_topping == "beef bbq pizza":
    topping_price = 65000
    price += 65000
    print(f"Topping price: {topping_price}")
elif chosen_topping == "chicken mayo pizza":
    topping_price = 60000
    price += 60000
    print(f"Topping price: {topping_price}")
elif chosen_topping == "pepperoni pizza":
    topping_price = 45000
    price += 45000
    print(f"Topping price: {topping_price}")
elif chosen_topping == "Tuna Mayo Pizza":
    topping_price = 65000
    price += 65000
    print(f"Topping price: {topping_price}")
else:
    print ("Invalid order!! We set to default.")
    chosen_topping == "original pizza"
    topping_price = 30000
    price += 30000
    print(f"Topping price: {topping_price}")
    
    
# Display crust choices
print("""\n==========CRUST==========""")
print("Pan Crust     |FREE ")
print("Thick Crust   |8,000 ")
print("Cheese Crust  |10,000 ")
print("Stuffed Crust |12,000 ")
print("Crown Crust   |15,000 ")
print("""==========================""")
chosen_crust = input("Chosen Crust: ")

# Check chosen crust and display the price
if chosen_crust == "pan crust":
    crust_price = 0
    price += 0
    print(f"Crust price: {crust_price}")
elif chosen_crust == "thick crust":
    crust_price = 8000
    price += 8000
    print(f"Crust price: {crust_price}")
elif chosen_crust == "cheese crust":
    crust_price = 10000
    price += 10000
    print(f"Crust price: {crust_price}")
elif chosen_crust == "stuffed crust":
    crust_price = 12000
    price += 12000
    print(f"Crust price: {crust_price}")
elif chosen_crust == "crown crust":
    crust_price = 15000
    price += 15000
    print(f"Crust price: {crust_price}")
else:
    print("Invalid order!! We set to default.")
    chosen_crust == "pan crust"
    crust_price = 0
    price += 0
    print(f"Crust price: {crust_price}")

# Display pizza size choices
print("""\n==========SIZE==========""")
print("Small          |FREE ")
print("Medium         |15,000 ")
print("Large          |20,000 ")
print("Extra Large    |25,000 ")
print("""=========================""")
chosen_size = input("Chosen pizza size: ")

# Check chosen size and display the price
if chosen_size == "small":
    size_price = 0
    price += 0
    print(f"Small size: {size_price}")
elif chosen_size == "medium":
    size_price = 15000
    price += 15000
    print(f"Medium size: {size_price}")
elif chosen_size == "large":
    size_price = 20000
    price += 20000
    print(f"Large size: {size_price}")
elif chosen_size == "extra large":
    size_price = 25000
    price += 25000
    print(f"Large size: {size_price}")
else:
    print("Invalid order!! We set to default.")
    chosen_size == "small"
    size_price = 0
    price += 0
    print(f"Small size: {size_price}")
    
# Ask if customer wants extra cheese
extra_cheese = input("\nDo you want extra cheese?(yes/no):")

# extra cheese price
extra_cheese_price = 13000

# Initialize variable for extra cheese summary
extra_cheese_summary = f"Extra Cheese\t\tRp.{extra_cheese_price}"

# Check if the customer wants extra cheese
if extra_cheese == "yes":
    extra_cheese_price = 13000
    price += 13000
    print(f"Extra Cheese: {extra_cheese_price}")
elif extra_cheese == "no":
    extra_cheese_price = 0
    price += 0
    print(f"No Extra Cheese: {extra_cheese_price}")
else:
    print ("Invalid order!! We set to default.")
    extra_cheese == "no"
    extra_cheese_price = 0
    price += 0
    print(f"No Extra Cheese: {extra_cheese_price}")

# Display summary of the order
print("\n========== YOUR ORDER SUMMARY ==========")
print(f"{chosen_topping:<20}   Rp {topping_price:>10}")
print(f"{chosen_crust:<20}   Rp {crust_price:>10}")
print(f"{chosen_size:<20}   Rp {size_price:>10}")

# Display extra cheese summary if chosen
if extra_cheese == "yes":
    print(f"Extra Cheese{'':<8}   Rp {extra_cheese_price:>10}")

# Display total cost
print("=========================================")
print(f"Total cost of your order: Rp {price:>10}")
print("=========================================")
print("Thank you for buying from Pizza Cuy!")

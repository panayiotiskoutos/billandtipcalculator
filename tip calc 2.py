#Panayiotis Koutos
#Bill and Tip calc


# Product prices
burger = 5.5
fries = 2
soft_drink = 1.5
pasta = 8
pizza = 10

# Ask quantities
burger_quantity = int(input("How many burgers? "))
fries_quantity = int(input("How many fries? "))
soft_drink_quantity = int(input("How many soft drinks? "))
pasta_quantity = int(input("How many pasta? "))
pizza_quantity = int(input("How many pizzas? "))

# Calculate bill
bill_amount = (
    burger_quantity * burger +
    fries_quantity * fries +
    soft_drink_quantity * soft_drink +
    pasta_quantity * pasta +
    pizza_quantity * pizza
)

print("Bill Amount: $", round(bill_amount, 2))

# Tip input and validation
while True:
    tip_percentage = float(input("Enter tip percentage: "))
    if tip_percentage < 0:
        print("Tip cannot be negative. Please enter a valid amount.")
    else:
        break

#convert to decimal
tip_percentage = tip_percentage / 100

# Calculate tip and total
tip_amount = bill_amount * tip_percentage
total_amount = bill_amount + tip_amount


print("Tip Amount: $", round(tip_amount, 2))
print("Total Amount: $", round(total_amount, 2))


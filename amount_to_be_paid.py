###
# 25% discount is charged for each product purchased over two
# Program that calculates the amount to be paid
# Read the number of purchased products and the product price 
# from the keyboard
# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00
##
no_of_products = int(input("Enter the number of purchased products: "))
price = float(input("Enter the price: "))
if no_of_products < 0:
    print("Invalid number, try again.")
elif no_of_products == 0:
    print("You haven't purchased anything!")
elif no_of_products <= 2:
    purchase = no_of_products * price
    print(f"You need to pay {purchase} PLN.")
elif no_of_products > 2:
    purchase = (2 * price) + (price * 0.75) * (no_of_products - 2)
    print(f"You need to pay {purchase} PLN.")
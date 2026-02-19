cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ").lower()
festival = input("Is it festival season? (yes/no): ").lower()

discount = 0

if cart_value >= 10000:
    discount = 10
elif cart_value >= 5000:
    discount = 5

if membership == "silver":
    discount = max(discount, 5)
elif membership == "gold":
    discount = max(discount, 10)
elif membership == "platinum":
    discount = max(discount, 15)

if festival == "yes":
    discount = max(discount, 20)

final_amount = cart_value - (cart_value * discount / 100)

print("Highest Discount Applied:", discount, "%")
print("Final Payable Amount: ₹", final_amount)
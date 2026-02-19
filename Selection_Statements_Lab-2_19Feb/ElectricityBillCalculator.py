units = int(input("Enter units consumed: "))
age = int(input("Enter age: "))

bill = 0

if units <= 100:
    bill = units * 5

elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

# Senior citizen discount
if age >= 60:
    bill = bill * 0.90   # 10% discount

print("Total Electricity Bill: ₹", bill)
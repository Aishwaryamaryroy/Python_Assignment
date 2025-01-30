#Exercise1
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

month_number = int(input("Enter the month: "))

if 1 <= month_number <= 12:
    print(f"Month {month_number} is {month_names[month_number - 1]}")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")



# Exercise2
age = int(input("Enter your age: "))
full_price = 6

if age < 16:
    ticket_price = full_price / 2
elif age >= 60:
    ticket_price = full_price / 3
else:
    ticket_price = full_price

print(f"Your ticket costs £{ticket_price}")

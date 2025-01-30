# Exercise 3
weight = float(input("Enter your weight in (kg): "))
height = float(input("Enter your height in (m): "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:}")

if bmi < 18.5:
    print("You are in the 'Underweight' range.")
elif 18.5 <= bmi < 25:
    print("You are in the 'Normal' range.")
elif 25 <= bmi < 30:
    print("You are in the 'Overweight' range.")
else:
    print("You are in the 'Obese' range.")

# Exercise 4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3
print(f"The greatest number is: {greatest}")

# Exercise 5
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print(f"The factorial of {num} is {factorial}")


# Exercise 6
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num //= 10

print(f"Reversed number: {reverse}")

# Exercise 7
num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print(f"Multiples of {num} up to {limit}:")
for i in range(1, (limit // num) + 1):
    print(num * i)

# Exercise 8
while True:
    value = input(":")
    if value.lower() == "done":
        print("Done")
        break
    else:
        print(value)

# Exercise 9
for i in range(1, 11):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Exercise 10
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()




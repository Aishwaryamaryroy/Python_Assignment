# Exercise 1
filename = input("Enter the filename: ")
file = open(filename, "r")
print(file.read())
file.close()

 #Exercise 2
source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")
file1 = open(source_file, "r")
file2 = open(destination_file, "w")
file2.write(file1.read())
file1.close()
file2.close()
print("File copied successfully.")

# Exercise 3
filename = input("Enter the filename: ")
file = open(filename, "r")
content = file.read()
file.close()
word_count = len(content.split())
print("Total words:", word_count)

#Exercise 4
try:
    user_input = input("Enter a number: ")
    num = int(user_input)
    print("Converted integer:", num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

#Exercise 5
user_input = input("Enter a list of integers (separated by spaces): ")
try:
    integers_list = [int(x) for x in user_input.split()]
    for num in integers_list:
        if num < 0:
            raise ValueError(f"Negative integer found: {num}")
    print("All integers are non-negative.")
except ValueError as e:
    print(f"Error: {e}")


#Exercise 6
try:
    input_numbers = input("Enter a list of integers separated by spaces: ").split()
    numbers = [int(num) for num in input_numbers]
    average = sum(numbers) / len(numbers)
    print("Average of the entered numbers:", average)
except ValueError:
    print("Invalid input! Please enter only integers.")
except ZeroDivisionError:
    print("Cannot compute average of an empty list.")
finally:
    print("Program has finished running.")

#Exercise 7
try:
    filename = input("Enter the filename: ")
    with open(filename, 'w') as file:
        file.write("Welcome to the file handling program!\n")
    print("File written successfully. Welcome!")
except Exception as e:
    print(f"An error occurred: {e}")


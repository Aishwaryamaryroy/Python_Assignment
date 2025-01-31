#Exercise 1
def compute(a, b=10, c=None):
    if c is None:
        print(a + b)
    else:
        print(a * b * c)

compute(5)
compute(5,20)
compute(5,20,2)

#Exercise 2

def filter_strings(str1):
    filtered_list = []
    for s in str1:
        if len(s) >= 5:
            filtered_list.append(s)
    return filtered_list


print(filter_strings(["apple", "cat", "banana", "dog", "elephant"]))

#Exercise 3
expression = "3 * 5 + 2"
result = eval(expression)
print(result)

#Exercise 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)


#Exercise 5
def to_uppercase(str1):
    return list(map(str.upper, str1))

print(to_uppercase(["apple", "banana", "cherry"]))








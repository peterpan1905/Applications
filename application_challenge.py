# Problem 1
input_string = input("Put something in as a string to be reversed? ")
reverse_string = input_string[::-1]
print(reverse_string)

# Problem 2
x = None
y = None
z = None

while True:
    try:
        x = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Please input an integer: ")

while True:
    try:
        y = int(input("Enter a second integer: "))
        break
    except ValueError:
        print("Please input a second integer: ")

while True:        
    try:
        z = int(input("Enter a third integer: "))
        break
    except ValueError:
        print("Please input a third integer: ")

def find_largest(x,y,z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
    
result = find_largest(x,y,z)
print(f"The largest of the three integers you input is {result}.")

# Problem 3
while True:
     try:
         n = int(input("Enter an integer to calculate the factorial: "))
         break
     except ValueError:
         print("Please input an integer to calculate the factorial: ")

def calc_factorial(n):
    if n == 0:
        return 1
    else:
        return n*calc_factorial(n-1)
    
factorial = calc_factorial(n)
print("The factorial of " + str(n) + " is " + str(factorial))

# Problem 4
def calc_fibonacci(n):
    if n in {0,1}:
        return n
    else:
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)
    
n = int(input("Which position of the Fibonacci Sequence would you like to calculate? "))
fibonacci_value = calc_fibonacci(n)
print(f"The value of the {n} position in the Fibonacci Sequence is {fibonacci_value}")
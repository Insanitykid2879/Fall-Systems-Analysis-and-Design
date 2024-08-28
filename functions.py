#M1HW Functions
#Alex Alejandro
#8/21/2024

def menu():
    print("Welcome to the Calculator Program")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit")
    return input("Enter a number: ")


def get_number_of_inputs(operation_name):
    while True:
        try:
            num_of_inputs = int(input(f"How many numbers do you want to {operation_name}? "))
            if num_of_inputs < 2:
                print("You need at least two numbers to perform this operation.")
            else:
                return num_of_inputs
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def add():
    num_of_inputs = get_number_of_inputs("add")
    numbers = []

    for i in range(num_of_inputs):
        try:
            number = float(input(f"Enter number {i +1}: "))
            numbers.append(number)

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return []
        
    return numbers






def calc_add(numbers):

    total = sum(numbers)
    return f"The sum of numbers is: {total}"



def sub():
    num_of_inputs = get_number_of_inputs("subtract")
    numbers = []

    for i in range(num_of_inputs):
        try:
            number = float(input(f"Enter number {i +1}: "))
            numbers.append(number)
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return []

    return numbers


def calc_sub(numbers):


    result = numbers[0]
    for number in numbers[1:]:
        result -= number

    return f"The result of subtraction is: {result}"


def div():
    num_of_inputs = get_number_of_inputs("divide")
    numbers = []

    for i in range(num_of_inputs):
        try:
            number = float(input(f"Enter number {i +1}: "))
            numbers.append(number)
            
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return []

    return numbers


def calc_div(numbers):
    try:
        result = numbers[0]
        for number in numbers[1:]:
            result /= number

        return f"The result of division is: {result}"

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."




def mul():
    num_of_inputs = get_number_of_inputs("divide")
    numbers = []

    for i in range(num_of_inputs):
        try:
            number = float(input(f"Enter number {i +1}: "))
            numbers.append(number)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            return []

    return numbers

    

def calc_mul(numbers):
    result = 1
    for number in numbers:
        result *= number

    return f"The result of multiplication is: {result}"

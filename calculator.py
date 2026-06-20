import math

history = []


def display_menu():
    print("\n========== PYTHON CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. View History")
    print("9. Save History")
    print("10. Exit")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a % b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        return "Error: Cannot calculate square root of a negative number."
    return math.sqrt(a)


while True:
    display_menu()

    choice = input("\nChoose an option (1-10): ")

    if choice in ["1", "2", "3", "4", "5", "6"]:

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        operations = {
            "1": ("+", add),
            "2": ("-", subtract),
            "3": ("*", multiply),
            "4": ("/", divide),
            "5": ("%", modulus),
            "6": ("**", power)
        }

        symbol, function = operations[choice]
        result = function(num1, num2)

        print("\nResult:", result)

        history.append(f"{num1} {symbol} {num2} = {result}")

    elif choice == "7":

        num = get_number("Enter a number: ")
        result = square_root(num)

        print("\nResult:", result)

        history.append(f"√{num} = {result}")

    elif choice == "8":

        print("\n========== HISTORY ==========")

        if history:
            for item in history:
                print(item)
        else:
            print("No calculations performed yet.")

    elif choice == "9":

        with open("history.txt", "w") as file:
            for item in history:
                file.write(item + "\n")

        print("\nHistory saved successfully to history.txt")

    elif choice == "10":

        save = input("Do you want to save history before exiting? (yes/no): ").lower()

        if save == "yes":
            with open("history.txt", "w") as file:
                for item in history:
                    file.write(item + "\n")
            print("History saved successfully.")

        print("\nThank you for using Python Calculator!")
        break

    else:
        print("\nInvalid choice! Please select a number between 1 and 10.")

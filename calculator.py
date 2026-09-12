"""
Simple CLI Calculator
A command-line calculator supporting basic arithmetic operations,
with input validation and a continuous REPL loop.
"""


def add(x: float, y: float) -> float:
    return x + y


def subtract(x: float, y: float) -> float:
    return x - y


def multiply(x: float, y: float) -> float:
    return x * y


def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def power(x: float, y: float) -> float:
    return x ** y


def modulo(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot modulo by zero.")
    return x % y


OPERATIONS = {
    "1": ("Add", add, "+"),
    "2": ("Subtract", subtract, "-"),
    "3": ("Multiply", multiply, "*"),
    "4": ("Divide", divide, "/"),
    "5": ("Power", power, "^"),
    "6": ("Modulo", modulo, "%"),
}


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Try again.")


def print_menu() -> None:
    print("\n=== CLI Calculator ===")
    for key, (name, _, symbol) in OPERATIONS.items():
        print(f"{key}. {name} ({symbol})")
    print("Q. Quit")


def main() -> None:
    print("Welcome to the CLI Calculator!")

    while True:
        print_menu()
        choice = input("\nChoose an operation: ").strip().upper()

        if choice == "Q":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice. Please try again.")
            continue

        name, func, symbol = OPERATIONS[choice]
        x = get_number("Enter first number: ")
        y = get_number("Enter second number: ")

        try:
            result = func(x, y)
            print(f"\nResult: {x} {symbol} {y} = {result}")
        except ZeroDivisionError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()

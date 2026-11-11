# ==========================================
# ENGINEERING UNIT CONVERTER
# ND1 PYTHON MINI PROJECT
# ==========================================

def display_menu():
    """Display the main menu."""
    print("\n================================")
    print("     ENGINEERING UNIT CONVERTER")
    print("================================")
    print("1. Millimetres to Inches")
    print("2. Inches to Millimetres")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Kilometres/hour to Metres/second")
    print("8. Metres/second to Kilometres/hour")
    print("9. Metres to Centimetres")
    print("10. Centimetres to Metres")
    print("11. View Conversion History")
    print("0. Exit")
    print("================================")


def get_number(prompt):
    """Get a valid numeric input from the user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def convert_units(choice, value):
    """Convert the given value based on the selected conversion option."""
    conversions = {
        1: lambda x: (x / 25.4, "inches"),
        2: lambda x: (x * 25.4, "millimetres"),
        3: lambda x: ((x * 9 / 5) + 32, "Fahrenheit"),
        4: lambda x: ((x - 32) * 5 / 9, "Celsius"),
        5: lambda x: (x * 2.20462, "pounds"),
        6: lambda x: (x / 2.20462, "kilograms"),
        7: lambda x: (x / 3.6, "metres/second"),
        8: lambda x: (x * 3.6, "kilometres/hour"),
        9: lambda x: (x * 100, "centimetres"),
        10: lambda x: (x / 100, "metres"),
    }

    if choice in conversions:
        return conversions[choice](value)
    return None, None


def save_history(history, choice, value, result, unit):
    """Save a conversion record in the history list."""
    conversion_names = {
        1: "Millimetres to Inches",
        2: "Inches to Millimetres",
        3: "Celsius to Fahrenheit",
        4: "Fahrenheit to Celsius",
        5: "Kilograms to Pounds",
        6: "Pounds to Kilograms",
        7: "Kilometres/hour to Metres/second",
        8: "Metres/second to Kilometres/hour",
        9: "Metres to Centimetres",
        10: "Centimetres to Metres",
    }

    label = conversion_names.get(choice, "Unknown conversion")
    record = f"{label}: {value} -> {result:.4f} {unit}"
    history.append(record)


def show_history(history):
    """Display the conversion history."""
    print("\n======= CONVERSION HISTORY =======")

    if not history:
        print("No conversions have been performed yet.")
    else:
        for index, record in enumerate(history, start=1):
            print(f"{index}. {record}")

    print("==================================")


def main():
    """Main program loop."""
    history = []

    print("Welcome to the Engineering Unit Converter!")

    while True:
        display_menu()

        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("Invalid selection! Please enter a number.")
            continue

        if choice == 0:
            print("\nThank you for using this program.")
            print("Goodbye!")
            break

        if choice == 11:
            show_history(history)
            continue

        if choice < 1 or choice > 11:
            print("Invalid option. Please choose a number between 0 and 11.")
            continue

        value = get_number("Enter the value to convert: ")
        result, unit = convert_units(choice, value)

        if result is not None:
            print("\n---------- RESULT ----------")
            print(f"Original value: {value}")
            print(f"Converted value: {result:.4f} {unit}")
            print("----------------------------")

            save_history(history, choice, value, result, unit)
        else:
            print("Conversion could not be completed.")


if __name__ == "__main__":
    main()

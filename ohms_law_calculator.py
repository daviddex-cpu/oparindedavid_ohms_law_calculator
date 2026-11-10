# Smart Ohm's Law & Power Calculator
# CTE123 Python Mini Project - ND1 Mechatronics Engineering, YabaTech
# Author: Dex Klein (Oparinde David)

def get_float(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than zero. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number only.")


def calculate():
    """Main calculation menu and logic."""
    print("\nWhat do you want to calculate?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")
    print("4. Power (P)")
    
    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        # Calculate Voltage: V = I × R
        current = get_float("Enter Current (A): ")
        resistance = get_float("Enter Resistance (Ω): ")
        voltage = current * resistance
        power = voltage * current
        result = f"Voltage = {voltage:.4f} V"
        details = f"I = {current} A, R = {resistance} Ω"

    elif choice == "2":
        # Calculate Current: I = V / R
        voltage = get_float("Enter Voltage (V): ")
        resistance = get_float("Enter Resistance (Ω): ")
        current = voltage / resistance
        power = voltage * current
        result = f"Current = {current:.4f} A"
        details = f"V = {voltage} V, R = {resistance} Ω"

    elif choice == "3":
        # Calculate Resistance: R = V / I
        voltage = get_float("Enter Voltage (V): ")
        current = get_float("Enter Current (A): ")
        resistance = voltage / current
        power = voltage * current
        result = f"Resistance = {resistance:.4f} Ω"
        details = f"V = {voltage} V, I = {current} A"

    elif choice == "4":
        # Calculate Power: P = V × I
        voltage = get_float("Enter Voltage (V): ")
        current = get_float("Enter Current (A): ")
        power = voltage * current
        result = f"Power = {power:.4f} W"
        details = f"V = {voltage} V, I = {current} A"
        resistance = voltage / current if current != 0 else 0

    else:
        print("Invalid choice. Please select 1, 2, 3 or 4.")
        return None

    # ---- OWN TWIST: Engineering tip based on power ----
    tip = get_power_tip(power)

    print("\n" + "="*45)
    print("RESULT")
    print("="*45)
    print(result)
    print(f"Details: {details}")
    print(f"Power   : {power:.4f} W")
    print("-"*45)
    print("Engineering Tip:")
    print(tip)
    print("="*45)

    return {
        "result": result,
        "power": power,
        "details": details
    }


def get_power_tip(power):
    """Return a practical engineering tip based on the power value."""
    if power < 0.1:
        return "Very low power → Safe for sensitive electronics & sensors."
    elif power < 0.5:
        return "Low power → Suitable for most small electronic circuits."
    elif power < 2:
        return "Medium power → Consider a small heat sink if continuous."
    elif power < 10:
        return "High power → Use proper heat sink and good ventilation."
    else:
        return "Very high power → Requires serious thermal management & safety."


def show_history(history):
    """Display the calculation history for this session."""
    if not history:
        print("\nNo calculations yet.")
        return

    print("\n" + "="*45)
    print("SESSION HISTORY")
    print("="*45)
    for i, item in enumerate(history, 1):
        print(f"{i}. {item['result']} | Power: {item['power']:.4f} W")
    print("="*45)


def main():
    print("="*50)
    print("   SMART OHM'S LAW & POWER CALCULATOR")
    print("="*50)
    print("Calculate Voltage, Current, Resistance or Power")
    print("with engineering tips and calculation history.\n")

    history = []   # stores results for this session

    while True:
        print("\nMain Menu:")
        print("1. New Calculation")
        print("2. View History")
        print("
... 
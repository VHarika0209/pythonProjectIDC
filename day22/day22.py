import argparse

def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit-32)*5/9
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def celsius_to_kelvin(celsius):
    return celsius + 273.15

def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    # Convert input to Celsius first
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == "Kelvin":
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError("Unsupported source unit.")

    #Convert Celsius to target unit
    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return celsius_to_fahrenheit(celsius)
    elif to_unit == "Kelvin":
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError("Unsupported source unit.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="🌡️ Convert temperatures between Celsius, Fahrenheit, and Kelvin."
    )
    parser.add_argument("value",type=float,help="Temperature value to convert.")
    parser.add_argument("from_unit", type = str, help = "input unit (Celsius, Fahrenheit, Kelvin).")
    parser.add_argument("to_unit", type=str, help = "Output unit (Celsius, Fahrenheit, Kelvin).")

    args = parser.parse_args()
    try:
        result = convert_temperature(args.value, args.from_unit, args.to_unit)
        print(f"\n✅ {args.value}° {args.from_unit.capitalize()} = {result:.2f}° {args.to_unit.capitalize()}")
    except Exception as e:
        print(f"❌ Error: {e}")

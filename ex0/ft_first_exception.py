def check_temperature(temp_str: str) -> None:
    try:
        temp = int(temp_str)
        if temp <= 40 and temp >= 0:
            return f"Temperature {temp}°C is perfect for plants!"
        elif temp > 40:
            return f"Error: {temp}°C is too hot for plants (max 40°C)"
        elif temp < 0:
            return f"Error: {temp}°C is too cold for plants (min 0°C)"
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"


def receive_input() -> None:
    print("=== Garden Temperature Checker ===\n")
    print("Testing temperature: 25")
    print(check_temperature("25"))

    print("\nTesting temperature: abc")
    print(check_temperature("abc"))

    print("\nTesting temperature: 100")
    print(check_temperature("100"))

    print("\nTesting temperature: -50")
    print(check_temperature("-50"))

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    receive_input()

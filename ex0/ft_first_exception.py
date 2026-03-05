#!/usr/bin/env python3


def check_temperature(temp_str: str) -> int:
    """
    Convert input entered to int and validate plant temperature
    returns temprature value if valid and valueError
    if the input is not a number or not in a range from (0 - 40)
    """
    try:
        temperature: int = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number \n")

    if temperature < 0:
        raise ValueError(
            f"Error: {temperature}°C is too cold for plants (min 0°C\n)"
        )

    if temperature > 40:
        raise ValueError(
            f"Error: {temperature}°C is too hot for plants (max 40°C \n)"
        )

    return temperature


def test_temperature_input() -> None:
    """
    Test different valid and invalid test cases
    """
    print("=== Garden Temperature Checker ===\n")

    test_values: list[str] = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Testing temperature: {value}")
        try:
            temp: float = check_temperature(value)
            print(f"Temperature {temp}°C is perfect for plants! \n")
        except ValueError as error:
            print(error)

    print("\nAll tests completed - program didn’t crash!")


if __name__ == "__main__":
    test_temperature_input()

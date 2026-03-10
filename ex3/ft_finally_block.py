#!/usr/bin/env python3

def water_plants(plant_list: str) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant == None:
                raise Exception("Cannot water None- invalid plant!")
            print(f"Watering {plant}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    valid_values = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(valid_values)
    print("Watering completed successfully!\n")

    invalid_values = ["tomato", None, "carrots"]
    print("Testing with error...")
    water_plants(invalid_values)


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\n Cleanup always happens, even with errors!")

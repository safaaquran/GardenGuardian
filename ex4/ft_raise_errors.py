#!/usr/bin/env python3

def check_plant_health(
    plant_name: str, water_level: int,
    sunlight_hours: int
) -> None:
    try:
        if plant_name == "":
            raise ValueError(" Plant name cannot be empty!")

        if not (0 < water_level < 11):
            raise ValueError(f"Water level {water_level} is too high (max 10)")

        if not (1 < sunlight_hours < 13):
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        print(f"Plant '{plant_name}' is healthy!\n")
    except ValueError as e:
        print(f"Error: {e} \n")


def test_plant_checks() -> None:
    print("Testing good values...")
    good_name = "tomato"
    check_plant_health(good_name, 7, 3)

    print("Testing empty plant name...")
    bad_name = ""
    check_plant_health(bad_name, 7, 3)

    print("Testing  bad water level...")
    bad_level = 15
    check_plant_health("tomato", bad_level, 3)

    print("Testing bad sunlight hours...")
    bad_sunlight = 0
    check_plant_health("tomato", 6, bad_sunlight)
    print("All error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()

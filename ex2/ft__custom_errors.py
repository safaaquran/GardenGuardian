#!/usr/bin/env python3


class GardenError(Exception):
    """Base exception for garden-related problems."""
    pass


class PlantError(GardenError):
    """Exception raised for plant problems."""
    pass


class WaterError(GardenError):
    """Exception raised for watering problems."""
    pass


def check_plant() -> None:
    """Simulate a plant problem."""
    raise PlantError("The tomato plant is wilting!")


def check_water() -> None:
    """Simulate a watering problem."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """Test the custom garden errors."""
    print("Testing PlantError...")
    try:
        check_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    print("Testing WaterError...")
    try:
        check_water()
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")

    try:
        check_plant()
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    try:
        check_water()
    except GardenError as error:
        print(f"Caught a garden error: {error}\n")


def main() -> None:
    """Run the demo."""
    print("=== Custom Garden Errors Demo ===\n")
    test_custom_errors()
    print("All custom error types work correctly")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        try:
            if plant_name == "":
                raise PlantError("Plant name cannot be empty!")

            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")

        except PlantError as error:
            print(f"Error adding plant: {error}\n")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant == "":
                    raise WaterError("Cannot water empty plant name")

                print(f"Watering {plant}- success")

        except WaterError as error:
            print(f"Error watering plant: {error}")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self,
        plant_name: str,
        water_level: int,
        sunlight_hours: int
    ) -> None:
        try:
            if plant_name == "":
                raise PlantError("Plant name cannot be empty!")

            if not (0 < water_level < 11):
                raise ValueError(
                    f"Water level {water_level} is too high (max 10)"
                )

            if not (1 < sunlight_hours < 13):
                raise ValueError(
                    f"Sunlight hours {sunlight_hours} is too low (min 2)"
                )

            print(
                f"{plant_name}: healthy (water: {water_level}, "
                f"sun: {sunlight_hours})"
            )

        except PlantError as error:
            print(f"Error checking {plant_name}: {error}")
        except ValueError as error:
            print(f"Error checking {plant_name}: {error}")

    def test_error_recovery(self) -> None:
        try:
            raise WaterError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...\n")


def main() -> None:
    manager = GardenManager()

    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("Watering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 8)

    print("\nTesting error recovery...")
    manager.test_error_recovery()

    print("Garden management system test complete!")


if __name__ == "__main__":
    main()

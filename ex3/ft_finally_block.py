class PlantError(Exception):
    pass


def water_plants(plant_list: list) -> None:
    try:
        print("Opening watering system")

        for plant in plant_list:
            if plant is None:
                raise PlantError(f"Cannot water {plant} - invalid plant!")

            print(f"Watering {plant}")

    except PlantError as error:
        print(f"Error: {error}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    plants = ["tomato", "lettuce", "carrots"]
    water_plants(plants)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    invalid_plants = ["tomato", None, "carrots"]
    water_plants(invalid_plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()

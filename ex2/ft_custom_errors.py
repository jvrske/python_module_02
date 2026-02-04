class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant():
    raise PlantError("The tomato plant is wilting!")


def check_water():
    raise WaterError("Not enough water in the tank!")


def test_errors():
    print("=== Custom Garden Errors Demo ===\n")

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
    for errors in (check_plant, check_water):
        try:
            errors()
        except GardenError as error:
            print(f"Caught a garden error: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()

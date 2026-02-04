class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant():
    def __init__(self, name: str, water_level: int, sun_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sun_hours = sun_hours


class GardenManager():
    def __init__(self) -> None:
        self.__plants = []
        self.__water_tank = 2

    def add_plant(self, plant: Plant) -> None:
        try:
            if not plant.name:
                raise PlantError("Plant name cannot be empty!")

            if plant.water_level < 1:
                raise PlantError(f"Water level {plant.water_level} \
is too low (min 1)")
            if plant.water_level > 10:
                raise PlantError(f"Water level {plant.water_level} \
is too high (max 10)")

            if plant.sun_hours < 2:
                raise PlantError(f"Sunlight hours {plant.sun_hours} \
is too low (min 2)")
            if plant.sun_hours > 12:
                raise PlantError(f"Sunlight hours {plant.sun_hours} \
is too high (max 12)\n")

            self.__plants.append(plant)
            print(f"Added {plant.name} successfully")
        except PlantError as error:
            print(f"Error adding plant: {error}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for p in self.__plants:
                if self.__water_tank == 0:
                    raise WaterError("Not enough water in tank")
                p.water_level += 1
                self.__water_tank -= 1
                print(f"Watering {p.name} - success")
        except WaterError as error:
            print(error)
        finally:
            print("Closing watering system (cleanup)")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    tomato = Plant("tomato", 5, 8)
    lettuce = Plant("lettuce", 10, 5)
    inv_name = Plant("", 5, 3)
    gm = GardenManager()
    gm.add_plant(tomato)
    gm.add_plant(lettuce)
    gm.add_plant(inv_name)

    print("\nWatering plants...")
    gm.water_plants()


if __name__ == "__main__":
    test_garden_management()

def garden_operations(case: int) -> None:
    if case == 0:
        try:
            int("abc")
        except ValueError:
            return "Caught ValueError: invalid literal for int()\n"
    elif case == 1:
        try:
            1 / 0
        except ZeroDivisionError:
            return "Caught ZeroDivisionError: division by zero\n"
    elif case == 2:
        try:
            open("file.txt")
        except FileNotFoundError:
            return "Caught FileNotFoundError: No such file 'file.txt'\n"
    elif case == 3:
        try:
            plants = {"tomato": 50}
            plants["sunflower"]
        except KeyError:
            return "Caught KeyError: 'missing\\_plant'\n"
    elif case == 4:
        try:
            int("bca")
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
            return "Caught an error, but program continues!\n"


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    print(garden_operations(0))

    print("Testing ZeroDivisionError...")
    print(garden_operations(1))

    print("Testing FileNotFoundError...")
    print(garden_operations(2))

    print("Testing KeyError...")
    print(garden_operations(3))

    print("Testing multiple errors together...")
    print(garden_operations(4))

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

#!/usr/bin/env python3

def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        age = int("safaa")
        print(age)
    except ValueError:
        print("Caught ValueError: invalid literal for int() \n")

    try:
        print("Testing ZeroDivisionError...")
        area = 10 / 0
        print(area)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        file = open("42file.txt")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file '42file.txt'\n")

    print("Testing KeyError...")
    try:
        plants = {"rose": 5, "tulip": 3}
        print(plants["Lilly"])
    except KeyError:
        print("Caught KeyError: 'Lilly'\n")

    print("Testing multiple errors together...")
    try:
        value = int("abc")
        result = 10 / value
        print(result)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def error_types_caller() -> None:
    print()
    garden_operations()
    print()


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    error_types_caller()
    print("All error types tested successfully!")

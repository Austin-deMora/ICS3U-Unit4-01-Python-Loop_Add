#!/usr/bin/env python3
#
# Created by: Austin de Mora
# Created on: May 2021
# This program uses a while loop to find a factorial


def main():
    # This function calculates the factorial of a number

    # Input
    positive_integer_string = input("Enter the positive integer you chose: ")
    print("")

    # process
    try:
        positive_integer = int(positive_integer_string)

        assert positive_integer > 0

        loop_counter = 0
        number_sum = 0

        while loop_counter < positive_integer:
            loop_counter = loop_counter + 1
            number_sum = number_sum + loop_counter

        print(number_sum)

    except AssertionError:
        print("Integer wasn't positive")
    except Exception:
        print("This was not an valid integer")


if __name__ == "__main__":
    main()

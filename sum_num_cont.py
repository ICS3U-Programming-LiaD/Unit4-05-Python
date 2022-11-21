#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Nov.11th, 2022
# This program lets the user tell it how many numbers
# they want to add together and then the user
# gives them the number they want to add
# and adds them together.


def main():

    # Initializing the counter and sum
    counter = 0
    sum = 0
    equation_string = ""

    # Asking the user for how many numbers they want to add up
    amount_numbers_to_add_up_as_string = input("How many numbers do you want to add? ")

    # Making sure the inputted number is valid
    try:
        amount_numbers_to_add_up = int(amount_numbers_to_add_up_as_string)
        if amount_numbers_to_add_up < 0:
            print("Please enter a positive number")
        else:
            try:
                while amount_numbers_to_add_up > counter:
                    # asking the user for the numbers they want to add together
                    numbers_to_add_together_as_string = input(
                        "What number would you like to add? "
                    )
                    numbers_to_add_together = int(numbers_to_add_together_as_string)
                    if numbers_to_add_together < 0:
                        print(numbers_to_add_together, " can't be added to the sum")
                        continue
                    else:
                        equation_string = (
                            equation_string + numbers_to_add_together_as_string + "+"
                        )
                        sum = numbers_to_add_together + sum
                        counter = counter + 1
                # Displaying the formula and the sum
                print(equation_string)
                print("Sum = {}".format(sum))
            except ValueError:
                print("Please enter a number!")

    except ValueError:
        print("Please enter a valid input")

    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()

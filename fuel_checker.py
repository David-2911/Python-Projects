def main():
    gauge = get_fraction("Fraction: ")
    fuel = percentage(gauge)
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel:.0f}%")


def get_fraction(prompt):
    while True:
        try:
            # Get the user input
            fraction = input(prompt).strip()

            # Split the input into numerator and denominator
            numerator, denominator = fraction.split('/')

            # Convert to floats and perform the division
            result = int(numerator) / int(denominator)

            if result <= 1:
                return result  # If successful, return the result

        except ValueError:
            # Handle the case where the input is not a number or can't be split
            print("Invalid input. Please enter a fraction in the form 'numerator/denominator'.")

        except ZeroDivisionError:
            # Handle the case where the denominator is zero
            print("Division by zero is not allowed. Please enter a valid fraction.")



def percentage(fraction):
    # Convert the fraction to a percentage
    return round(fraction * 100)


if __name__ == '__main__':
    main()

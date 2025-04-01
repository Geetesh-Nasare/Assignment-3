import math
user = int(input("Enter a number: "))

try: 
    number = float(user)

    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    print(f"Square root: {square_root}")
    print(f"Logarithm: {natural_log}")
    print(f"Sine: {sine_value}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")    
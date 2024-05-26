import argparse

# Operators available in the train game
OPERATORS = ['+','-','*','/','**']

def check_input(value):
    """Check that the argument passed to the script is an integer between 0 and 10,000"""
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is an invalid value. Must be an int.")
    
    if ivalue < 0 or ivalue > 10_000:
        raise argparse.ArgumentTypeError(f"{value} is an invalid value. Must be an int between 0 and 10000.")
    return ivalue

def split_digits(num):
    """Take an input int between 0 and 10,000 and convert it to a list of four int digits"""
    padded_number = f"{num:04}"
    return [int(digit) for digit in padded_number]

def operation(a, b, op):
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b != 0:
                return a / b
            else:
                return "Error"
        elif op == '**':
            # Handle cases where 0 cannot be raised to a negative power
            if a == 0 and b < 0:
                return "Error"
            # Handle large exponentiation values
            if a < 0 and not float(b).is_integer():
                return "Error"
            result = a ** b
            if result > 10_000 or result < -10_000 or isinstance(result, complex):
                return "Error"
            return result
    except (OverflowError, ValueError, ZeroDivisionError):
        return "Error"
    return "Error"

def make_ten(numbers, trace=[]):
    """
    Loop through list of digits in pairs, combine the pair using an operation, pass the new list recursively
    to the make_ten function until there is only one number left in the list. Check if it is 10. 
    """
    if len(numbers) == 1:
        if numbers[0] == 10:
            print(f"Possible!")
            print("Steps:")
            for step in trace:
                print(step)
            return True
        return False
    
    # Loop up to the 2nd last element
    for i in range(len(numbers) - 1):
        for op in OPERATORS:
            result = operation(numbers[i], numbers[i+1], op)
            if result == "Error":
                continue

            # Create a copy of the input numbers list to modify
            new_numbers = numbers[:]
            
            # Replace the first digit of the pair with the pairs combination, and drop the second digit
            new_numbers[i] = result
            new_numbers = new_numbers[:i+1] + new_numbers[i+2:]

            # Record the current step
            new_trace = trace + [(f"{numbers[i]} {op} {numbers[i+1]} = {result}")]
            if make_ten(new_numbers, new_trace):
                return True
    return False

def main():
    # Take in an argument: An integer between 0 and 10,000
    parser = argparse.ArgumentParser(description="Process a number between 0 and 10000.")
    parser.add_argument('number', type=check_input, help="An integer between 0 and 10000")
    args = parser.parse_args()
    digits = split_digits(args.number)
    if not make_ten(digits):
        print("No solution found")

if __name__ == "__main__":
    main()

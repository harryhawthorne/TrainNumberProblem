import argparse
from itertools import permutations, product
import logging

OPERATORS = ['+','-','*','/']

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def check_input(value):
    """
    Check that the argument passed to the script is an integer between 0 and 10,000
    """
    try:
        ivalue = int(value)
    except:
        raise argparse.ArgumentTypeError(f"{value} is an invalid value. Must be an int.")
    
    if ivalue < 0 or ivalue > 10_000:
        raise argparse.ArgumentTypeError(f"{value} is an invalid value. Must be an int between 0 and 10000.")
    return ivalue

def split_digits(num):
    padded_number = f"{num:04}"
    return [int(digit) for digit in padded_number]

def operation(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        if b != 0:
            return a/b
        else:
            return "Error"
    else:
        return "Invalid operator"


def make_ten(numbers, trace=[]):
    if len(numbers) == 1:
        if numbers[0] == 10:
            print(f"Possible!")
            print("Steps:")
            for step in trace:
                print(step)
            return True
        return False
    for i in range(len(numbers) - 1):
        for op in OPERATORS:
            result = operation(numbers[i],numbers[i+1], op)
            if result == "Error":
                continue
            new_numbers = numbers[:]
            new_numbers[i] = result
            new_trace = trace + [(f"{numbers[i]} {op} {numbers[i+1]} = {result}")]
            new_numbers = new_numbers[:i+1] + new_numbers[i+2:]
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
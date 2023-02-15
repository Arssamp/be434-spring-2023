#!/usr/bin/env python3
"""
Author : Alexis
Date   : 2023-02-15
Purpose: sum up numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='sum up numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    # Update the input so there is one argument that takes positional 
    # arguments from the command line. Make sure you add a line that says
    # you need one or more arguments from the user with nargs="+"
    # delete all the rest of the arguments (you just need one)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Sum up numbers; print the sum statement and total"""

    args = get_args()

    # get all of the numbers from the command line
    numbers = args.numbers

    # create a variable to calculate the total, set to 0

    # create an empty list for storing the numbers as strings
    
    for num in numbers:

        # add the number to the total

        # create a new variable that converts the number to a string, use str()

        # add the new variable to the list from above

    # create the "sum up" phrase for printing, e.g. "1 + 2 + 3"
    # note that "numbers_as_srtings" is the name of the list from above
    sum_up = ' + '.join(numbers_as_strings)

    # write a print statement that prints the "sum up" phrase, and the total

# --------------------------------------------------
if __name__ == '__main__':
    main()

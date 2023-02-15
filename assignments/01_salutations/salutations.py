#!/usr/bin/env python3
"""
Author : asampson1 <asampson1@localhost>
Date   : 2023-02-15
Purpose: say hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='say hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='A greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='A name to greet',
                        metavar='str',
                        type=str,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='A boolean flag for excited',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start of program"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    excited = args.excited

    phrase = greeting + ', ' + name 

    if excited:
        print(phrase + '!')
    else: 
        print(phrase + '.') 


# --------------------------------------------------
if __name__ == '__main__':
    main()

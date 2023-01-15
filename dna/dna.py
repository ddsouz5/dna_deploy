#!/usr/bin/env python3
"""
Author : ddsouz5 <ddsouz5@gmail.com>
Date   : 2023-01-15
Purpose: Count the number of occurences of a DNA String
"""

import argparse
import os
from typing import NamedTuple

def count_sequence(dna) -> str:
    dna_dict = {
            'A': 0,
            'T': 0,
            'G': 0,
            'C': 0
            }
    #print(dna)
    dna_list = list(dna)
    for c in dna_list:
        if c in dna_dict:
            dna_dict[c] += 1

    return (dna_dict['A'],
            dna_dict['T'],
            dna_dict['C'],
            dna_dict['G'])

# -------------------------------------------------
class Args(NamedTuple):
    """ Command-line arguments """
    dna: str

# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Count the number of occurences of a DNA String',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='DNA Sequence',
                        help='A DNA Sequence such as ACTGGTAC')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).readline().rstrip().upper()
    else:
        args.dna = args.dna.rstrip().upper()

    return Args(args)


# --------------------------------------------------
def main() -> None:
    """ Run """

    args = get_args()
    dna_arg = args.dna

    #print(f'dna = "{dna_arg}"')
    dna_dict = count_sequence(dna_arg.dna)
    print('A:{}, T:{}, C:{}, G:{}'.format(dna_dict[0], dna_dict[1],
        dna_dict[2], dna_dict[3]))

# --------------------------------------------------
if __name__ == '__main__':
    main()

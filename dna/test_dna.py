"""
Unit test for dna program
"""
import dna
import os
from subprocess import getstatusoutput

PRG = 'dna.py'

def test_cmdline1() -> None:
    assert (1, 1, 1, 1) == dna.count_sequence('ACTG')

def test_cmdline2() -> None:
    assert (0, 0, 0, 0) == dna.count_sequence('oofbnvm')

def test_exists() -> None:
    """ Program exists """
    assert os.path.exists(PRG)

def test_input1() -> None:
    """ input file 1 """
    retval, out = getstatusoutput(f'./{PRG} tests/input1.txt')
    assert retval == 0
    assert out == 'A:225, T:251, C:245, G:249' 

def test_input1() -> None:
    """ input file 2 """
    retval, out = getstatusoutput(f'./{PRG} tests/input2.txt')
    assert retval == 0
    assert out == 'A:1, T:1, C:4, G:1'

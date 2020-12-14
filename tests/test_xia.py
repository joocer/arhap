"""
Note that this is testing randomness functions, failure is inevitable on a
long enough series of tests (think billions)
"""
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import xia
import collections


def test_random_string():

    """ test the string is the right length """
    rnd_str = xia.random_string(length=32, characters='abc')
    assert len(rnd_str) == 32
    
    """ test the string only has the recquested chars """
    counter = collections.Counter(rnd_str)
    if 'a' in counter:
        counter.pop('a')
    if 'b' in counter:
        counter.pop('b')
    if 'c' in counter:
        counter.pop('c')
    assert len(counter) == 0


def test_random_int():

    rnd_1 = xia.random_int()
    rnd_2 = xia.random_int()

    assert not rnd_1 == rnd_2
    assert isinstance(rnd_1, int) 


def test_random_range():

    vals = []
    for i in range(5000):
        vals.append(xia.random_range(10,20))

    assert min(vals) == 10, "test lower extreme of range"
    assert max(vals) == 20, "test upper extreme of range"


def test_bytes_to_int():

    b1 = [0] * 8
    assert (xia.bytes_to_int(b1) == 0)

    b2 = [255] * 4
    assert (xia.bytes_to_int(b2) == (2**32 - 1))

    b3 = [255] * 8
    assert (xia.bytes_to_int(b3) == (2**64 - 1))


def test_random_choice():
    
    options = ['one', 'two', 'three']

    for i in range(100):
        choice = xia.random_choice(options)
        assert choice in options


if __name__ == "__main__":
    test_random_string()
    test_random_int()
    test_random_range()
    test_bytes_to_int()
    test_random_choice()

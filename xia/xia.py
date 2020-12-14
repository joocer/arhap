import os

def random_string(length=64, characters=string.ascii_letters + string.digits):
    result_str = ''.join(random_choice(characters) for i in range(length))
    return result_str

def random_int():
    """
    Select a random integer (64bit)
    """
    return bytes_to_int(os.urandom(8))

def random_range(min, max):
    """
    Select a random integer between two numbers
    """
    return (random_int() % ((max + 1) - min)) + min

def bytes_to_int(bytes):
    """
    Helper function, convert set of bytes to an integer
    """
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

def random_choice(options):
    """
    Select an item from a list of values
    """
    r = random_range(0, len(options) - 1)
    return options[r]

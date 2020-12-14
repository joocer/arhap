import os
import string
from typing import Any, Union

def random_string(
        length:int = 64,
        characters:str = string.ascii_letters + string.digits) -> str:
    result_str = ''.join(random_choice(characters) for i in range(length))
    return result_str

def random_int() -> int:
    """
    Select a random integer (64bit)
    """
    return bytes_to_int(os.urandom(8))

def random_range(min:int, max:int) -> int:
    """
    Select a random integer between two numbers
    """
    return (random_int() % ((max + 1) - min)) + min

def bytes_to_int(bytes: bytes) -> int:
    """
    Helper function, convert set of bytes to an integer
    """
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

def random_choice(options: Union[list, str]) -> Any:
    """
    Select an item from a list of values
    """
    r = random_range(0, len(options) - 1)
    return options[r]

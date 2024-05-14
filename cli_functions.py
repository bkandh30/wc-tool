import typing
import os

def byte_count(file) -> int:
    """
    Returns the number of bytes
    Args:
        file: File object
    Returns:
        int: Number of bytes in the file
    """
    return os.path.getsize(file)

def line_count(file) -> int:
    """
    Returns the number of lines
    Args:
        file: File object
    Returns:
        int: Number of lines in the file
    """
    lines = file.split('\n')
    return len(lines)-1

def word_count(file) -> int:
    """
    Returns the number of words
    Args:
        file: File object
    Returns:
        int: Number of words in the file
    """
    words = file.decode().split()
    return len(words)

def char_count(file) -> int:
    """
    Returns the number of characters
    Args:
        file: File object
    Returns:
        int: Number of characters in the file
    """
    chars = file.decode()
    return len(chars)
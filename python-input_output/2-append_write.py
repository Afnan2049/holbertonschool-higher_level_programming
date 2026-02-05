#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appends a string to a UTF8 and returns the number of the characters added.

    Args:
        filename (str): The name of the file to append on.
        text (str): The text to append on the file.

        Returns:
            int: The number of charecters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)

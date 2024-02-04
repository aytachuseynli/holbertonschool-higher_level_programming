#!/usr/bin/python3
"""
  Text indentation
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    lines = []

    current_line = ''
    for char in text:
        current_line += char
        if char in separators:
            lines.append(current_line.strip())
            lines.append('\n')
            current_line = ''

    if current_line:
        lines.append(current_line.strip())

    print(''.join(lines))

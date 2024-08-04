#!/usr/bin/python3

"""
module that checks if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Function that checks if all boxes can be opened.

    Args:
    - boxes (list of lists): List of  list contains keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if type(boxes) is not list or len(boxes) == 0:
        return False
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    box = [0]
    while box:
        key = box.pop()
        for new_key in boxes[key]:
            if new_key < n and not opened[new_key]:
                opened[new_key] = True
                box.append(new_key)
    return all(opened)

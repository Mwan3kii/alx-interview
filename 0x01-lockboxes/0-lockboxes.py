#!/usr/bin/python3
"""Method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of list of int): Each inner list has keys to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, otherwise False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
    return all(unlocked)

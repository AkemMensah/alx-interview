#!/usr/bin/python3

"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Return True if can be open, false if not
    """
    number_of_keys = [0]
    number_of_boxes = len(boxes)

    for keys in number_of_keys:
        for box in boxes[keys]:
            if box < number_of_boxes and box not in number_of_keys:
                number_of_keys.append(box)
    if len(number_of_keys) == number_of_boxes:
        return True
    return False

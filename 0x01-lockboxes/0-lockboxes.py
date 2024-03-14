#!/usr/bin/python3
"""This is a module to solve the locked boxes inteerview question"""


def canUnlockAll(boxes):
    """This is a function to unlock boxes"""
    sum_boxs = len(boxes)
    unlocked_boxes = [False] * sum_boxs
    unlocked_boxes[0] = True
    my_keys = [key for key in boxes[0] if key < sum_boxs]

    while my_keys:
        curr_key = my_keys.pop()
        if not unlocked_boxes[curr_key]:
            unlocked_boxes[curr_key] = True
            my_keys.extend([key for key in boxes[curr_key] if key < sum_boxs])

    return all(unlocked_boxes)

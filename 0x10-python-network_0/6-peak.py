#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (int): List of integers to find a peak of.
    Returns:
        int or None: Peak element of the list, or None if the list is empty.
    """
    size = len(list_of_integers)
    middle_elem = size
    middle = size // 2

    if size == 0:
        return None

    while True:
        middle_elem = middle_elem // 2
        if (middle < size - 1 and
                list_of_integers[middle] < list_of_integers[middle + 1]):
            if middle_elem // 2 == 0:
                middle_elem = 2
            middle = middle + middle_elem // 2
        elif middle_elem > 0 and list_of_integers[middle] < list_of_integers[middle - 1]:
            if middle_elem // 2 == 0:
                middle_elem = 2
            middle = middle - middle_elem // 2
        else:
            return list_of_integers[middle]

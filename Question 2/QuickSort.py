# Implementation of quicksort

"""
function to find the partition position.
element smaller than pivot are on the left.
element greater than pivot are on the right.
"""


def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # assign pointer for greater element
    i = low - 1

    # traverse and compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found_candidates
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping i with j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i  # + 1


"""
function to perform quicksort
"""


def quick_sort(array, low, high):
    if low < high:
        # Find pivot element such that
        part = partition(array, low, high)

        # Recursive call on the left and right of the pivot
        quick_sort(array, low, part - 1)
        quick_sort(array, part + 1, high)

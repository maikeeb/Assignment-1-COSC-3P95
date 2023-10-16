import random

from QuickSort import quick_sort

"""
Create a random array and test quick sort to see if there are any bugs
"""


def random_testing():
    # create a random array
    ran_array = random_array()
    print("Random Scrambled Array:")
    print(ran_array)

    # sort the array using quick sort
    quick_sort(ran_array, 0, len(ran_array) - 1)
    print("Sorted Array using quick sort")
    print(ran_array)

    # test if the array was sorted correctly
    testing_case = True
    error_list = []

    # test if every number is greater or equal to the number to the left of it
    for i in range(1, len(ran_array) - 1):
        if ran_array[i] < ran_array[i - 1]:
            testing_case = False
            error_list.append(i)

    # Print to console error if any are found
    print("The sorting algorithm was correct") if testing_case else print("The sorting algorithm was incorrect")

    if not testing_case:
        print("The errors found are at the following indices")
        print(error_list)


"""
Create an array of a random size and random elements
"""


def random_array() -> []:
    data = []
    for i in range(0, random.randint(1, 10000)):
        data.append(random.randint(1, 10000))

    return data


random_testing()

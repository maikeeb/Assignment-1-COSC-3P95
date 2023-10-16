# implementation of delta debugging

from Question5CodeSnippet import processString

"""
recursive function to find delta debugging of a test case (smallest form of case with same bug)

iterates through all the char in the string and detects if the character is needed for the bug to still exist
"""


def delta_debugging(input_string, index):
    if index < len(input_string):

        temp_string = [*input_string]
        del temp_string[index]
        temp_string = "".join(temp_string)

        # get string from working function and bugged function if we remove at the index
        answer_found = processString(temp_string)
        correct_answer = processStringWorking(temp_string)

        # compares function results
        if answer_found != correct_answer:
            delta_debugging(temp_string, index)  # if not the same remove character from the index

        else:
            # if the bug no longer exists return the character and move the index over 1
            delta_debugging(input_string, index + 1)
    else:
        print("Delta: " + input_string)
        return input_string


"""
Changed the function to work and not to have the bug to check answers against
"""


def processStringWorking(input_str):
    output_str = ""
    for char in input_str:
        if char.isupper():
            output_str += char.lower()
        else:
            output_str += char.upper()

    return output_str


# list of test cases given
test_cases = ["abcdefG1", "CCDDEExy", "1234567b", "8665"]

# cycle through all test cases from question
for case in test_cases:
    print("Test case: " + case)
    delta_debugging(case, 0)

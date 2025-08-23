
'''
Challenge: Optimize the function to handle large input lists efficiently.
==============================
Description: Develop a function called find_common_elements that takes two lists as input and returns a new list containing elements that are common to both input lists.
'''


def find_common_elements(list1, list2):
    try:
        if len(list1) < len(list2):
            set1, other_list = set(list1), list2
        else:
            set1, other_list = set(list2), list1

        common = list(set1 & set(other_list))

    except TypeError:
        print("TypeError: One or both inputs are not iterable")
        return[]

    return common

list1 = [1, 2, 3, 4, 5]
list2 = [3, 3, 4, 5, 6, 7]

print("Execution Completed")
print("Common elements are:", find_common_elements(list1, list2))














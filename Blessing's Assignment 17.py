
'''
Challenge: Ensure that the function works correctly with tuples of different lengths.
=============================================
Description: Create a function called concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples.
'''


def concat_tuples(tuple1, tuple2):
    try:
        if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
            raise TypeError("Both inputs must be tuples")

        result = tuple1 + tuple2

    except TypeError as e:
        print("TypeError:", e)
        return ()

    return result

t1 = (1, 2, 3, 4, 5)
t2 = (3, 3, 4, 5, 6, 7)

print("Execution Completed")
print("Concat_tuple is:", concat_tuples(t1, t2))